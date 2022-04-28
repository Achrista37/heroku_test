#Dependencies
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd
import json
from flask import Flask, jsonify,render_template
from flask_cors import CORS

 # Create engine using the database file
engine = create_engine("sqlite:///Resources/internet.sqlite")

#Reflect Database
Base = automap_base()
Base.prepare(engine, reflect = True)

#Create session
session = Session(engine)

#################################################
# Flask Setup
#################################################
#app.config["CACHE_TYPE"] = "null"
app = Flask(__name__)
CORS(app)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
            f"Available Routes:<br/>"
            f"/api/dashboard"
            )


# API Pages
@app.route("/api/dashboard")
def api_overview():
   dbConnect = engine.connect()
   df = pd.read_sql('select * from Internet_data_hpfl', dbConnect)
   json_overview = json.loads(df.to_json(orient='records'))
   dbConnect.close()
   return jsonify(json_overview)

# #
# @app.route("/")
# def home():

#     # Return template and data
#     return render_template("index.html")
# #





if __name__ == "__main__":
    app.run(debug=True)

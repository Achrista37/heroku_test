#Dependencies
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd
import json
from flask import Flask, jsonify,render_template

 # Create engine using the database file
engine = create_engine("postgres://ogbxrcxjrgzqrq:b25ce739808e8d95ea3c8a196fb367e6c91f0e53272303bfdc0e58b9a501d254@ec2-3-223-213-207.compute-1.amazonaws.com:5432/ddmpo72ifhij51")

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
   df = pd.read_sql('select * from internet_with_countrycodes', dbConnect)
   json_overview = json.loads(df.to_json(orient='records'))
   dbConnect.close()
   return jsonify(json_overview)

#################################################
# HTML Routes
#################################################

# @app.route('/html')
# def index():
#     return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

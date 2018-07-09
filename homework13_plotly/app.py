# import necessary libraries
import pandas as pd

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import (Flask, render_template, jsonify)

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///DataSets/belly_button_biodiversity.sqlite")
# reflect an existing database into a new model
# copies table strucutres from database structure as it already exixts
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

#print all the calsses mapped to the base
Base.classes.keys()

Otu=Base.classes.otu
Samples=Base.classes.samples
Samples_metabdata =Base.classes.samples_metadata

inspector = inspect(engine)

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# Returns the dashboard homepage
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/names')
def names():
    """Return a list of sample names."""

    # Use Pandas to perform the sql query
    stmt = session.query(Samples).statement
    df = pd.read_sql_query(stmt, session.bind)
    df.set_index('otu_id', inplace=True)

    # Return a list of the column names (sample names)
    return jsonify(list(df.columns))


# @app.route('/otu')
# def otu():
#     otu_results = session.query(Otu.lowest_taxonomic_unit_found).all()
#     otus = []
    
#     for result in otu_results:
#         otus.append(result)
#     print(otus)
#     return jsonify(otus)

if __name__ == "__main__":
    app.run(debug=True)




import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import datetime as dt


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
measurement = Base.classes.measurement
station1 = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

# welcome page with list of options
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/yyyy-mm-dd (start date)<br/>"
        f"/api/v1.0/yyyy-mm-dd/yyyy-mm-dd (start date/end date)"
    )

# list of precipitations
@app.route("/api/v1.0/precipitation")
def precip():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query date and precipitation from all rows 
    results = session.query(measurement.date, measurement.prcp).all()

    session.close()

    # Convert list of tuples into normal list
    all_measure = []
    for date, prcp in results:
        measure_dict = {}
        measure_dict["Date"] = date
        measure_dict["Prcp"] = prcp
        all_measure.append(measure_dict)

    return jsonify(all_measure)

# list of stations
@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all info from station
    results = session.query(station1.id, station1.station, station1.name, station1.latitude, station1.longitude, station1.elevation).all()

    session.close()

    # Convert list of tuples into normal list
    all_station = []
    for id, station, name, latitude, longitude, elevation in results:
        station_dict = {}
        station_dict["ID"] = id
        station_dict["Station"] = station
        station_dict["Name"] = name
        station_dict["Latitude"] = latitude
        station_dict["Longitude"] = longitude
        station_dict["Elevation"] = elevation
        all_station.append(station_dict)

    return jsonify(all_station)

# last year of data
@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # set dates
    start_date = dt.date(2017, 8, 23)
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    # Query dates and tobs for station within date
    results = session.query(measurement.date, measurement.tobs).\
    filter(measurement.station == "USC00519281").\
    filter(measurement.date >= query_date).\
    filter(measurement.date <= start_date).all()

    session.close()

    # Convert list of tuples into normal list
    all_tob = []
    for date, tobs in results:
        tob_dict = {}
        tob_dict["Date"] = date
        tob_dict["TOBS"] = tobs
        all_tob.append(tob_dict)

    return jsonify(all_tob)

# stats from a start date
@app.route('/api/v1.0/<date>')
def startdate(date):
    
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # query for stats
    min = session.query(func.min(measurement.tobs)).filter(measurement.date >= date)
    max = session.query(func.max(measurement.tobs)).filter(measurement.date >= date)
    avg = session.query(func.avg(measurement.tobs)).filter(measurement.date >= date)
    
    session.close()

    # create list
    all_start = [{"Min: " : min[0][0]},{"Max: " : max[0][0]},{"Average:" : avg[0][0]}]

    return jsonify(all_start)

# stats in a time frame
@app.route('/api/v1.0/<start>/<end>')
def timeframe(start,end):
    
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # query for stats
    min = session.query(func.min(measurement.tobs)).filter(measurement.date >= start).filter(measurement.date <= end)
    max = session.query(func.max(measurement.tobs)).filter(measurement.date >= start).filter(measurement.date <= end)
    avg = session.query(func.avg(measurement.tobs)).filter(measurement.date >= start).filter(measurement.date <= end)
    
    session.close()

    # create list
    all_frame = [{"Min: " : min[0][0]},{"Max: " : max[0][0]},{"Average:" : avg[0][0]}]

    return jsonify(all_frame)


if __name__ == '__main__':
    app.run(debug=True)


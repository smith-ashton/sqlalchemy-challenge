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

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/yyyy-mm-dd (start date)"
        f"/api/v1.0/yyyy-mm-dd/yyyy-mm-dd (start date/end date)"
    )


@app.route("/api/v1.0/precipitation")
def precip():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all passengers
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

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all passengers
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

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all passengers
    start_date = dt.date(2017, 8, 23)
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
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


@app.route('/api/v1.0/<date>')
def startdate(date):
    
    session = Session(engine)

    min = session.query(func.min(measurement.tobs)).filter(measurement.date >= date)
    max = session.query(func.max(measurement.tobs)).filter(measurement.date >= date)
    avg = session.query(func.avg(measurement.tobs)).filter(measurement.date >= date)
    
    session.close()

    all_start = [{"Min: " : min[0][0]},{"Max: " : max[0][0]},{"Average:" : avg[0][0]}]

    return jsonify(all_start)

@app.route('/api/v1.0/<start>/<end>')
def timeframe(start,end):
    
    session = Session(engine)

    min = session.query(func.min(measurement.tobs)).filter(measurement.date >= start).filter(measurement.date <= end)
    max = session.query(func.max(measurement.tobs)).filter(measurement.date >= start).filter(measurement.date <= end)
    avg = session.query(func.avg(measurement.tobs)).filter(measurement.date >= start).filter(measurement.date <= end)
    
    session.close()

    all_frame = [{"Min: " : min[0][0]},{"Max: " : max[0][0]},{"Average:" : avg[0][0]}]

    return jsonify(all_frame)


if __name__ == '__main__':
    app.run(debug=True)


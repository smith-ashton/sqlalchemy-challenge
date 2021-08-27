# sqlalchemy-challenge
## Step 1 - Climate Analysis and Exploration
Using SQLAlchemy, create a connection to the database and reflect the tables into classes. Link Python to the database to conduct the following analysis:
### Precipitation Analysis
Find the last date in the database and use it to retrieve the last year's worth of precipitation data. Load the data into a database and plot it using Matplotlib.
### Station Analysis
Find the station with the most observations and find the lowest, highest and average temp for that station. Create a histogram of the temperatures for the samestation across the last year.
## Step 2 - Climate App
Design a Flask API with the following pages:
<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-Homepage
<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;list all routes avaiable
<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-/api.v1.0/precipitation
<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;list all dates and its precipitation
<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-/api.v1.0/stations
<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;list all stations and their info
<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-/api.v1.0/tobs
<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;list all date and temperature observations from the most active station over the last year
<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-/api.v1.0/{start}
<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;list min, max, and avg temp for all days beginning with the input date
<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-/api.v1.0/{start}/{end}
<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;list min, max, and avg temp within specified date range

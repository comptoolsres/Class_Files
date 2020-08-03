# flights.May2018-April2020.csv and flights.May2017-Apr2018.csv Metadata

## Information about the flights.May2018-April2020.csv and flights.May2017-Apr2018.csv file

### File availability

These two files are too large to host in github. They are available via these Dropbox links:

* [`flights.May2017-Apr2018.csv`](https://www.dropbox.com/s/jizx4ijnpxmi3av/flights.May2017-Apr2018.csv?dl=0)
* [`flights.May2018-April2020.csv`](https://www.dropbox.com/s/r9ygw12bp2f6aml/flights.May2018-April2020.csv?dl=0)

These files contain US commercial flight on-time arrival information from the [Bureau of Transportation Statistics](https://www.transtats.bts.gov/DL_SelectFields.asp).

The data are from two time frames:

* `flights.May2017-Apr2018.csv`: data are from May 2017 to April 2018. Downloaded July 19, 2018.
* `flights.May2018-April2020.csv`: data are from May 2018 to April 20202. Downloaded July 31, 2020.

Unfortunately, one of the data columns in the two files is different. For the 2017-2018 data, the second column is a numeric code for the airline. While in the 2018-2020 data, it is a letter code for the airline. The rest of the columns should be identical. But due to the difference, the two files were not combined.

The columns in the dataset are in the table below.

Column header | Description
--------------|------------
FL_DATE | Date of the flight
2017-2018 file: AIRLINE_ID <br><br> 2018-2020 file: OP_UNIQUE_CARRIER | An identification number assigned by US DOT to identify a unique airline (carrier). <br><br> Unique Carrier Code
ORIGIN | Origin Airport
ORIGIN_CITY_NAME | Origin Airport, City Name **Note that this column has a comma in it**
ORIGIN_STATE_ABR | Origin Airport, State Code
DEST | Destination Airport
DEST_CITY_NAME | Destination Airport, City Name **Note that this column has a comma in it**
DEST_STATE_ABR | Destination Airport, State Code
DEP_TIME | Actual Departure Time (local time: hhmm)
DEP_DELAY_NEW | Difference in minutes between scheduled and actual departure time. Early departures set to 0.
DEP_DEL15 | Departure Delay Indicator, 15 Minutes or More (1.00=Yes, 0.00=No)
ARR_TIME | Actual Arrival Time (local time: hhmm)
ARR_DELAY_NEW | Difference in minutes between scheduled and actual arrival time. Early arrivals set to 0.
ARR_DEL15 | Arrival Delay Indicator, 15 Minutes or More (1.00=Yes, 0.00=No)
CANCELLED | Cancelled Flight Indicator (1=Yes)
CANCELLATION_CODE | Specifies The Reason For Cancellation
DIVERTED | Diverted Flight Indicator (1=Yes)
AIR_TIME | Flight Time, in Minutes
FLIGHTS | Number of Flights
DISTANCE | Distance between airports (miles)
CARRIER_DELAY | Carrier Delay, in Minutes
WEATHER_DELAY | Weather Delay, in Minutes
NAS_DELAY | National Air System Delay, in Minutes
SECURITY_DELAY | Security Delay, in Minutes
LATE_AIRCRAFT_DELAY | Late Aircraft Delay, in Minutes

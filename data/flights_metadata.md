# flights.May2017-Apr2018.csv Metadata

## Information about the flights.May2017-Apr2018.csv file.

This file contains US commercial flight information from the [Bureau of Transportation Statistics](https://www.transtats.bts.gov/DL_SelectFields.asp).
The data are from May of 2017 to April of 2018.


Data were downloaded July 19, 2018.


The columns in the dataset are in the table below.

Column header | Description
--------------|------------
FL_DATE | Date of the flight
AIRLINE_ID | An identification number assigned by US DOT to identify a unique airline (carrier). A unique airline (carrier) is defined as one holding and reporting under the same DOT certificate regardless of its Code, Name, or holding company/corporation.
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

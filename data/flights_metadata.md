# Flights Metadata

## Information about the flights files

### File availability

These files are too large to host in github. They are available via these Dropbox links:



These files contain US commercial flight on-time arrival information from the [Bureau of Transportation Statistics](https://www.transtats.bts.gov/DL_SelectFields.asp).

The columns in the dataset are in the table below.

Column #|Column header | Description
--------|--------------|------------
1|Year | Year of the flight |
2|Quarter | Quarter of the flight |
3|Month | Month of the flight |
4|DayofMonth | Calendar day of the flight |
5|DayofWeek | Day of the week (Monday=1, Tuesday=2, etc.)|
6|Flight Date | YYYY-MM-DD
7|Reporting_Airline | IATA code	for airline
8|Tail_Number | Aircraft tail number
9|Flight_Number_Reporting_Airline | Flight number (without IATA code)
10|Origin | Origin Airport code
11|OriginCityName | Origin Airport, City Name **Note that this column has a comma in it**
12|OriginState | Origin State Code
13|Dest | Destination Airport
14|DestCityName | Destination Airport, City Name **Note that this column has a comma in it**
15|DestState | Destination State Code
16|DepTime | Actual Departure Time (local time: hhmm)
17|DepDelay | Difference in minutes between scheduled and actual departure time. Early departures are negative.
18|DepDelayMinutes | Difference in minutes between scheduled and actual departure time. Early departures set to 0.
19|DepDel15 | Departure Delay Indicator, 15 Minutes or More (1.00=Yes, 0.00=No)
20|ArrTime | Actual Arrival Time (local time: hhmm)
21|ArrDelay|Difference in minutes between scheduled and actual arrival time. Early arrivals are negative.
22|ArrDelayMinutes | Difference in minutes between scheduled and actual arrival time. Early arrivals set to 0.
23|ArrDel15 | Arrival Delay Indicator, 15 Minutes or More (1.00=Yes, 0.00=No)
24|Cancelled | Cancelled Flight Indicator (1=Yes)
25|CancellationCode | Specifies The Reason For Cancellation
26|Diverted | Diverted Flight Indicator (1=Yes)
27|AirTime | Flight Time, in Minutes
28|Flights | Number of Flights
29|Distance | Distance between airports (miles)
30|CarrierDelay | Carrier Delay, in Minutes
31|WeatherDelay | Weather Delay, in Minutes
32|NASDelay | National Air System Delay, in Minutes
33|SecurityDelay | Security Delay, in Minutes
34|LateAircraftDelay | Late Aircraft Delay, in Minutes

### Flight data download and pre-processing





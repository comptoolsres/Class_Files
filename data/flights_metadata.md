# Flights Metadata

## Information about the flights files

### File availability

These files are too large to host in github. They are available via these Dropbox links:

* [`flights.May2017-Apr2018.csv`](https://www.dropbox.com/s/jizx4ijnpxmi3av/flights.May2017-Apr2018.csv?dl=0)
* [`flights.May2018-April2020.csv`](https://www.dropbox.com/s/r9ygw12bp2f6aml/flights.May2018-April2020.csv?dl=0)
* [`flights.May2020-April2022.csv`](https://www.dropbox.com/s/v6ntmpxn7n3pt67/flights.May2020-April2022.csv?dl=0)

These files contain US commercial flight on-time arrival information from the [Bureau of Transportation Statistics](https://www.transtats.bts.gov/DL_SelectFields.asp).

The data are from two-year time frames:

* `flights.May2017-Apr2018.csv`: data are from May 2017 to April 2018. Downloaded July 19, 2018.
* `flights.May2018-April2020.csv`: data are from May 2018 to April 2020. Downloaded July 31, 2020.
* `flights.May2020-April2022.csv`: data are from May 2020 to April 2022. Downloaded August 1st, 2022.

Unfortunately, one of the data columns in the files is different. For the 2017-2018 data, the second column is a numeric code for the airline. While in the 2018-2020 and 2020-2022 data, it is a letter code for the airline. The rest of the columns should be identical. But due to the difference, the files were not combined.

The columns in the dataset are in the table below.

Column #|Column header | Description
--------|--------------|------------
1|FL_DATE | Date of the flight
2|2017-2018 file: AIRLINE_ID <br><br> 2018-2020 file: OP_UNIQUE_CARRIER | An identification |number assigned by US DOT to identify a unique airline (carrier). <br><br> Unique Carrier Code
3|ORIGIN | Origin Airport
4|ORIGIN_CITY_NAME | Origin Airport, City Name **Note that this column has a comma in it**
5|ORIGIN_STATE_ABR | Origin Airport, State Code
6|DEST | Destination Airport
7|DEST_CITY_NAME | Destination Airport, City Name **Note that this column has a comma in it**
8|DEST_STATE_ABR | Destination Airport, State Code
9|DEP_TIME | Actual Departure Time (local time: hhmm)
10|DEP_DELAY_NEW | Difference in minutes between scheduled and actual departure time. Early departures set to 0.
11|DEP_DEL15 | Departure Delay Indicator, 15 Minutes or More (1.00=Yes, 0.00=No)
12|ARR_TIME | Actual Arrival Time (local time: hhmm)
13|ARR_DELAY_NEW | Difference in minutes between scheduled and actual arrival time. Early arrivals set to 0.
14|ARR_DEL15 | Arrival Delay Indicator, 15 Minutes or More (1.00=Yes, 0.00=No)
15|CANCELLED | Cancelled Flight Indicator (1=Yes)
16|CANCELLATION_CODE | Specifies The Reason For Cancellation
17|DIVERTED | Diverted Flight Indicator (1=Yes)
18|AIR_TIME | Flight Time, in Minutes
19|FLIGHTS | Number of Flights
20|DISTANCE | Distance between airports (miles)
21|CARRIER_DELAY | Carrier Delay, in Minutes
22|WEATHER_DELAY | Weather Delay, in Minutes
23|NAS_DELAY | National Air System Delay, in Minutes
24|SECURITY_DELAY | Security Delay, in Minutes
25|LATE_AIRCRAFT_DELAY | Late Aircraft Delay, in Minutes

### Flight data download and pre-processing

The flight data needs to be downloaded month by month from: [https://www.transtats.bts.gov/DL_SelectFields.aspx?gnoyr_VQ=FGJ&QO_fu146_anzr=b0-gvzr](https://www.transtats.bts.gov/DL_SelectFields.aspx?gnoyr_VQ=FGJ&QO_fu146_anzr=b0-gvzr)

I manually added the year and month to the filename. Then combined the files with these commands for the 2020-2022 data:

```bash
head -n1 T_ONTIME_REPORTING_2020_05.csv >  flights_May2020-April2022.csv
tail -n +2 T_ONTIME_REPORTING_202* >> flights_May2020-April2022.csv
```

:grimacing: Opps...that ends up with lines for each filename...should have used something like:

```bash
for file in T_ONTIME_REPORTING_202*
do 
tail -n +2 $file>> flights_May2020-April2022.csv
done

```

Since I had already deleted the individual files by the time I realized this, I cleaned up the `flights_May2020-April2022.csv` file with: `sed -i '/T_ONTIME_REPORTING_/d' flights.May2020-April2022.csv` That deleted the lines that had `T_ONTIME_REPORTING_` in them.




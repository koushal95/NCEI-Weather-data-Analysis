# NCEI-Weather-data-Analysis
Analysis of Weather data provided by NCEI using Spark.

This project performs analysis on the weather data collected by National Centers for Environmental Information (NCEI). The analysis includes statistical information on minimum temperatures, maximum temperatures, top hottest and coldest weather stations, hottest and coldest days that are observed. The results are reported after handling the abnormalities and missing information from the data. This project uses 18 years of data (from 2000 to 2018) that is provided by NCEI.

### Dataset
The dataset is made available publicly by NCEI. The dataset separated by year can be downloaded [here](https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/by_year/). The dataset contains attributes ID, date, element, value, m-flag, q-flag, s-flag, and observation time. Detailed information about the attributes can be found at ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt

Below is information to get a quick grasp on the attributes. 
* ID = 11-character station identification code 
* YEAR/MONTH/DAY = 8-character date in YYYYMMDD format (e.g. 19860529 = May 29, 1986) 
* ELEMENT = 4-character indicator of element type 
* DATA VALUE = 5-character data value for ELEMENT 
* M-FLAG = 1-character Measurement Flag 
* Q-FLAG = 1-character Quality Flag 
* S-FLAG = 1-character Source Flag 
* OBS-TIME = 4-character time of observation in hour-minute format (i.e. 0700 =7:00 am) 


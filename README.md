# ECCC_hourly_station_data_download
This script automates the downloading process of hourly meteorological data from Environment and Climate Change Canada

This script requires a 'input.txt' file that contains your needed stations following the format below:

##### Sample input.txt file starts ###### 
StationName = Pelly
StationID = 3448
StartYear = 1986
EndYear = 2015
outputdirectory = ./test_data/

StationName = Pelly2
StationID = 3449
StartYear = 1986
EndYear = 2015
outputdirectory = ./test_data/

##### Sample input.txt file ends ###### 

Note that the station id is NOT the one you see on climate id which is what is shown on the website
The station id is hidden, but can be found in the url when viewing climate data for a site, this is the id number you must use.
The file station_inventory_Canada.csv has a list of these; they get changed often so in the future this may break down and need to be recreated

Output:
After download, each year of data is stored in a seperate csv file.

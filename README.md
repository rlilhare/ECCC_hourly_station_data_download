# ECCC_hourly_station_data_download
This script automates the downloading process of hourly meteorological data from Environment and Climate Change Canada

This script requires a 'input.txt' file that contains your needed stations and can be found in this repo.

Note that the station id used in the input.txt file is NOT the one you see on climate id which is what is shown on the website
The station id is hidden, but can be found in the url when viewing climate data for a site, this is the id number you must use.
The file station_inventory_Canada.csv has a list of these; they get changed often so in the future this may break down and need to be recreated

Output:
After download, each year of data is stored in a seperate .csv file.

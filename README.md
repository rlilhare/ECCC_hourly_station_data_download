# ECCC_hourly_station_data_download
to make virtual environments:
    install pipenv: $ sudo apt install pipenv
    to create virtual environment: pipenv --python 3.8
    to activate pipenv environment: pipenv shell

to install requirements: make install_requirements

Before using this script, please read these instructions carefully:
This script automates the downloading process of hourly meteorological data from the Environment and Climate Change Canada database.
This script requires a 'input.txt' file that contains your required stations and can be found in this repo (ECCC_meterological_stations_inventory_Canada.csv).

Note that the station id used in the input.txt file is NOT the one you see on climate id which is what is shown on the website
The station id is hidden, but can be found in the url when viewing climate data for a site, this is the id number you must use.
The file ECCC_meterological_stations_inventory_Canada.csv has a list of these; they get changed often so in the future this may break down and need to be recreated

Output:
After download, each year of data is stored in a seperate .csv file.

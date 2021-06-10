import urllib.request
import os

with open('input.txt') as f:
    stns = f.readlines()

for stationNum in range(0, len(stns)):
    if stationNum % 6 == 0:
        name = stns[stationNum]
        stnID = stns[stationNum+1]
        startYear = stns[stationNum+2]
        endYear = stns[stationNum+3]
        outputLocation = stns[stationNum+4]

        name = name.strip()
        stnID = stnID.strip()
        startYear = startYear.strip()
        endYear = endYear.strip()
        outputLocation = outputLocation.strip()

        name = name[14:len(name)]
        stnID = stnID[12:len(stnID)]
        startYear = startYear[12: len(startYear)]
        endYear = endYear[10: len(endYear)]
        outputLocation = outputLocation[18:len(outputLocation)]

        print(name)

        for year in range(int(startYear), int(endYear)+1):
            for month in range(1, 12+1):
                response = urllib.request.urlopen('http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=' + stnID + '&Year=' + str(year) + '&Month=' + str(month) + '&Day=11&timeframe=1&submit=Download+Data')
                fileData = response.read()

                print(str(year) + " month: " + str(month))

                if not os.path.exists(outputLocation + name):
                    os.makedirs(outputLocation + name)

                with open(outputLocation + name + '/' + name + '_' + str(year) + '_month_' + str(month) + '.csv', "wb") as text_file:
                        text_file.write(fileData)

from pysolar.solar import *
import matplotlib.pyplot as plt
# import datetime
from datetime import *
import numpy as np 
from scipy import stats

average_degree = None
altitudes = []
azimuths = []

monthRange = None

def dtz(long):

    if -180 < long < -150:
        return -10
    elif -150 <= long < -135:
        return -9
    elif -135 <= long < -120:
        return -8
    elif -120 <= long < -105:
        return -7
    elif -105 <= long < -90:
        return -6
    elif -90 <= long < -75:
        return -5
    elif -75 <= long < -60:
        return -4
    elif -60 <= long < -45:
        return -3
    elif -45 <= long < -22:
        return -2
    elif -22 <= long < -7:
        return -1
    elif 150 <= long <= 180:
        return 10
    elif 135 <= long < 150:
        return 9
    elif 120 <= long < 135:
        return 8
    elif 105 <= long < 120:
        return 7
    elif 90 <= long < 105:
        return 6
    elif 75 <= long < 90:
        return 5
    elif 60 <= long < 75:
        return 4
    elif 45 <= long < 60:
        return 3
    elif 22 <= long < 45:
        return 2
    elif 7 <= long < 22:
        return 1
    else:
        return 0

   
    
    

#get degree position of sun
def getSunPos(userLat, userLong, userHemisphere):

    #passed in in ./main
    latitude = userLat
    longitude = userLong
    

    #class datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
    #limit = 1-2021

    #scatter plot x
    # x = []

    global monthRange

    #set ranges for data collection
    yearRange = range(2000, 2021)
    if userHemisphere == 'north':
        monthRange = range(4, 9)
    elif userHemisphere == 'south':
        monthRange = range(8, 13)
        
    dayRange = range(1, 29)

    #for every day of every month of every year specified, append data to positions
    #then, append positions and times of year to scatterplot 
    
    for yr in yearRange:
        for mo in monthRange:
            for d in dayRange:
                date = datetime(yr, mo, d, 12, 1, 1, 133320, tzinfo=timezone(timedelta(hours=dtz(longitude))))
                
                altitudes.append(get_altitude(latitude, longitude, date))
                # x.append("{}".format(mo) + " / " + "{}".format(d))
                azimuths.append(get_azimuth(latitude, longitude, date))
                

    #print the data to console
    # print('Altitudes:', altitudes)
    # print('Azimuths:', azimuths)

    #find std and percentile specified, then print
    standardAltitudeDeviation = np.std(altitudes)
    print('Standard Deviation Altitudes:', standardAltitudeDeviation)
    
    standardAzimuthDeviation = np.std(azimuths)
    print('Standard Deviation Azimuths:', standardAzimuthDeviation)

    most_common_degree = stats.mode(altitudes, keepdims=True)
    
    
    print('Common Altitudes:', most_common_degree)
    print('Average Altitudes:', average_degree)

    return monthRange
    # # set scatterplot y axis to data collected,
    # y = altitudes

    # # show scatterplot using the given axes
    # plt.scatter(x, y)
    # plt.show()

    # # debug print for axes
    # print("X:", x, "Y:", y)

# prediction engine

monthDictionary = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

def get_month_range(mnrange):
    m = [*mnrange]

    temp = []

    converted_range = ""

    for mnth in m:
        try:
            temp.append(monthDictionary.get(mnth))
            
        except (KeyError):
            print("Key not found in dict")
        

    for mnth in temp:
        if temp.index(mnth) != len(temp)-1:
            converted_range += f"{mnth}, "
        else:
            converted_range += mnth
            
    return converted_range

    

def update_avg_degree():
    global average_degree 
    test_var = np.mean(altitudes)
    average_degree = test_var
    return average_degree




"""
    UTC-12:00 - International Date Line West - 180 degrees longitude
    UTC-11:00 - Samoa Time Zone - 165 degrees longitude
    UTC-10:00 - Hawaii-Aleutian Time Zone - 150 degrees to 180 degrees longitude
    UTC-09:30 - Marquesas Islands Time Zone - 142.5 degrees longitude
    UTC-09:00 - Alaska Time Zone - 135 degrees to 150 degrees longitude
    UTC-08:00 - Pacific Time Zone - 120 degrees to 135 degrees longitude
    UTC-07:00 - Mountain Time Zone - 105 degrees to 120 degrees longitude
    UTC-06:00 - Central Time Zone - 90 degrees to 105 degrees longitude
    UTC-05:00 - Eastern Time Zone - 75 degrees to 90 degrees longitude
    UTC-04:00 - Atlantic Time Zone - 60 degrees to 75 degrees longitude
    UTC-03:30 - Newfoundland Time Zone - 52.5 degrees to 60 degrees longitude
    UTC-03:00 - Amazon Time Zone - 45 degrees to 60 degrees longitude
    UTC-02:00 - Fernando de Noronha Time Zone - 22.5 degrees to 37.5 degrees longitude
    UTC-01:00 - Azores Time Zone - 7.5 degrees to 22.5 degrees longitude
    UTC+00:00 - Greenwich Mean Time Zone - 7.5 degrees West to 7.5 degrees East longitude
    UTC+01:00 - Central European Time Zone - 7.5 degrees East to 22.5 degrees East longitude
    UTC+02:00 - Eastern European Time Zone - 22.5 degrees East to 37.5 degrees East longitude
    UTC+03:00 - Moscow Time Zone - 37.5 degrees East to 52.5 degrees East longitude
    UTC+03:30 - Iran Time Zone - 52.5 degrees East to 67.5 degrees East longitude
    UTC+04:00 - Gulf Time Zone - 52.5 degrees East to 67.5 degrees East longitude
    UTC+04:30 - Afghanistan Time Zone - 67.5 degrees East to 82.5 degrees East longitude
    UTC+05:00 - Pakistan Time Zone - 67.5 degrees East to 82.5 degrees East longitude
    UTC+05:30 - Indian Standard Time Zone - 82.5 degrees East to 97.5 degrees East longitude
    UTC+05:45 - Nepal Time Zone - 82.5 degrees East to 97.5 degrees East longitude
    UTC+06:00 - Bangladesh Time Zone - 97.5 degrees East to 112.5 degrees East longitude
    UTC+06:30 - Cocos Islands Time Zone - 97.5 degrees East to 112.5 degrees East longitude
    UTC+07:00 - Indochina Time Zone - 112.5 degrees East to 127.5 degrees East longitude
    UTC+08:00 - China Time Zone - 120 degrees East to 135 degrees East longitude
    UTC+08:45 - Southeastern Western Australia Time Zone - 117.5 degrees East to 132.5 degrees East longitude
    UTC+09:00 - Japan Time Zone - 135 degrees East to 150 degrees East longitude
"""
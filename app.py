from sunmodel import getSunPos

# Import Meteostat library and dependencies
from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily
from geopy.geocoders import Nominatim
from scipy import stats


def main(userCity):

    # setting up geolocation decoder
    geolocator = Nominatim(user_agent="MyTestApp")
    
    # user input to get string of location to decode to lat/long format
    locationInput = userCity
    
    # decoding of turning string to lat/long format
    locationDecode = geolocator.geocode(locationInput)
    print('Lat/Long:', locationDecode.latitude, locationDecode.longitude)
    
    # Set time period
    start = datetime(2000, 1, 1)
    end = datetime(2020, 12, 28)

    #create point for the decoded location
    location = Point(locationDecode.latitude, locationDecode.longitude)
    
    # Get daily data for designated location, start, and end
    datas = Daily(location, start, end)
    data = datas.fetch()
    
    # PySolar module
    
    if locationDecode.latitude > 0:
        hemisphere = 'north'
        print('hem: north')
    elif locationDecode.latitude <= 0:
        hemisphere = 'south'
        print('hem: south')
        
    mn = getSunPos(locationDecode.latitude, locationDecode.longitude, hemisphere)

    return [mn, locationDecode.latitude, locationDecode.longitude, userCity]
    
    # Plot line chart including average temperature
    # data.plot(y=['tavg'])
    # plt.show()
# Match sunset with current time

LATITUDE = 13.78
LONGITUDE = 100.59

from tkinter import *
import requests
import datetime

lat_long_data = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_latitude = float(lat_long_data.json()['iss_position']['latitude'])
iss_longitude = float(lat_long_data.json()['iss_position']['longitude'])

above_me = False

if (LATITUDE >= iss_latitude - 5 and LATITUDE <= iss_latitude + 5) and (LONGITUDE >= iss_longitude - 5 and LONGITUDE <= iss_longitude + 5):
    above_me = True

parameters = {
    "lat": LATITUDE,
    "lng": LONGITUDE,
    'formatted': 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
sunset = response.json()['results']['sunset']
sunrise = response.json()['results']['sunrise']

current_time = datetime.datetime.now().hour + 7
print(current_time)
sunrise_time = int(sunrise.split('T')[1].split(':')[0])
sunset_time = int(sunset.split('T')[1].split(':')[0])

print(sunrise_time)
print(sunset_time)
print()
print(response.json())

if (above_me):
    if (current_time < sunrise_time or current_time > sunset_time):
        print('its ngiht')

    elif (current_time > sunrise_time and current_time < sunset_time):
        print('it;s morning')


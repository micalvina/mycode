import requests
import datetime
import reverse_geocoder as rg

eoss = 'http://api.open-notify.org/iss-now.json'

resp = requests.get(eoss)
data = resp.json()

print(data)

position = data['iss_position']
latitude = position['latitude']
longitude = position['longitude']
time = data['timestamp']
ts = datetime.datetime.fromtimestamp(time)

    # return an ordered dictionary using our lat/lon vars
locator_resp= rg.search((latitude, longitude))

    # slice that object to return the city name only
city= locator_resp[0]["name"]

    # slice the object again to return the country
country= locator_resp[0]["cc"]

print(f'CURRENT LOCATION OF THE ISS:\n Lon: {longitude}\n Lat: {latitude}\n Timestamp: {ts}\n City/Country: {city}, {country}')


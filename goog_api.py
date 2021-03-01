# extract static google maps image

import requests

with open('gmap_api_key.txt', 'r') as file: # extract api key
    api_key = file.read()
file.close()

address = 'Singapore'
zoom = 10

url = "https://maps.googleapis.com/maps/api/staticmap?center={}&zoom={}&size=400x400&key={}".format(address, zoom,
                                                                                                    api_key)

r = requests.get(url)
f = open('{}.png '.format(address), 'wb')

f.write(r.content)

f.close()

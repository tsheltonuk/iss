import requests
import json
import googlemaps
from datetime import datetime
import webbrowser as wb

now = datetime.now()

print("Here is some location data about the ISS..." + '\n')

def iss():
	# Pull ISS location data
	url = "http://api.open-notify.org/iss-now.json"
	request = requests.get(url)
	resp = request.json()

	isspos = resp['iss_position']
	isslong = resp['iss_position']['longitude']
	isslat = resp['iss_position']['latitude']

	print("As of: " + (now.strftime("%d-%m-%Y %H:%M")))
	print("Current position: " + isslat + ', ' + isslong)


	# Query gmaps Places API to pin point ISS location
 	# in resepct to earth
	gapikey = '.....'
	gmaps = googlemaps.Client(key=gapikey)
	re = gmaps.places(isslat + ', ' + isslong)

	print("Which is over: " + (json.dumps(re['results'][0]['formatted_address'], indent=4)))
	print('\n')

	answ = raw_input("Would you like to open in GMAPS? (yes/no):")
	if answ == "yes":
		# open web browser and go to location in google maps
		wb.open('https://google.com/maps/place/'+isslat+'' + ',' + ''+isslong+'')
	else:
		exit()


iss()


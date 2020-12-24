# Real time ISS tracker

import json
import urllib.request
import turtle
import geocoder
import os
from time import sleep
from time_converter import *


screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic("world-map.gif")

screen.register_shape("iss.gif")
iss = turtle.Turtle()
iss.shape("iss.gif")
iss.setheading(45)
iss.penup()

while True:
	# Getting information about astronauts
	url = "http://api.open-notify.org/astros.json"
	response = urllib.request.urlopen(url)
	result = json.loads(response.read())
	print(f"There are currently {result['number']} in space : \n")
	people = result['people']
	for p in people:
		print(f"{p['name']} on board of {p['craft']}")

	url1 = "http://api.open-notify.org/iss-now.json"
	response1 = urllib.request.urlopen(url1)
	result1 = json.loads(response1.read())
	
	location = result1['iss_position']
	lat, lon = float(location['latitude']), float(location['longitude'])

	print(f"Current position of International Space Station\nLatitude : {lat}\nLongitude : {lon}")

	g = geocoder.ip('me').latlng
	my_lat, my_lon = g[0], g[1]

	my_location = turtle.Turtle()
	my_location.penup()
	my_location.color('Red')
	my_location.goto(my_lon, my_lat)
	my_location.dot(5)
	
	url2 = f"http://api.open-notify.org/iss-pass.json?lat={my_lat}&lon={my_lon}"
	response2 = urllib.request.urlopen(url2)
	result2 = json.loads(response2.read())
	unix_time = result2['request']['datetime']
	time = unixTimeToHumanReadable(unix_time)
	
	print(f"ISS is expected to pass above you at : {time}")

	iss.goto(lon, lat)
	
	sleep(5)
	os.system('clear')
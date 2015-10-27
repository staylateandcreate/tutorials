import requests

openweatherurl = 'http://api.openweathermap.org/data/2.5/weather?q='

location = raw_input('What weather are you interested in? Give me a location: ')

complete_url = openweatherurl + location

celsius = '&units=metric'
fahrenheit = '&units=imperial'

units_pref = raw_input("What units do you want? Type 'c' for celsius or 'f' for fahrenheit")

valid_input = False

while valid_input != True:
	if units_pref == 'c':
		complete_url += celsius
		valid_input = True
	elif units_pref == 'f':
		complete_url += fahrenheit
		valid_input = True
	else:
		print "Invalid. Please try again. Remember, your input must be 'c' or 'f'."
		units_pref = raw_input("What units do you want? Type 'c' for celsius or 'f' for fahrenheit")

page = requests.get(complete_url)

pagejson = page.json()

weather = pagejson['main']

temp = weather['temp']
hum = weather['humidity']

print 'The temperature in ' + location + ' is ' + str(temp)
print 'The humidity in ' + location + ' is ' + str(hum) 

The temperature in orindais 69.96
The humidity in orindais 74


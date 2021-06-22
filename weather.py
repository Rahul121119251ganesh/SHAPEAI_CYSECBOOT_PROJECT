import requests
#import os
from datetime import datetime

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
h="Weather Stats for - {}  || {}".format(location.upper(), date_time)
i="\nCurrent temperature is: {:.2f} deg C".format(temp_city)
j="\nCurrent weather desc  : {}".format(weather_desc)
k="\nCurrent Humidity      : {} %".format(hmdt)
l="\nCurrent wind speed    : {}kmph ".format(wind_spd)
m="\n-------------------------------------------------------------\n"

r=open('output.txt','w')
a=(m)
b=(h)
c=(m)
d=(i)
e=(j)
f=(k)
g=(l)
r.write(a)
r.write(b)
r.write(c)
r.write(d)
r.write(e)
r.write(f)
r.write(g)
r.close()


# Date: 12/17/20
# Abstarct: Program that web scrapes a calstrans website for weather data. This data is then manipulated 
#     into a string of integers which is sent to a method that encodes the given string.
# File: main.py

# Packages needed to run this portion of the program
# pip  opencv-python
# opencv-contrib-python
# pip install BeautifulSoup4 pandas selenium
# pip install geopy

# Imports
import cv2
from bs4 import BeautifulSoup
import requests
import geocoder
import socket
import base64
import liveScrape

# Definition to send the string weather variable to a base64 encoder
def num_to_alpha(num):
    num = hex(num)[2:].rstrip("L")
    if len(num) % 2:
        num = "0" + num

    return base64.b64encode(num.encode())

# Url is set to a specific website that contains weather data for a Highway traffic camera
url = "https://cwwp2.dot.ca.gov/vm/js/wx/d5/sr1imjinparkway.js"

# html_content is set to grab the information on the website and send it into a text format (list)
html_content = requests.get(url).text

# Parses the text data
soup = BeautifulSoup(html_content, 'html.parser')
camera_data = str(soup.contents[0][0:600])
camera_data_list = camera_data.split('\n')

# Sets variables to hold the values at their respective variable name/data
# Strings are adjusted to remove sybols and unessesary data
localDate = camera_data_list[0][23:-2]
localTime = camera_data_list[1][23:-6]
temperatureHigh = camera_data_list[8][23:-2]
temperatureLow = camera_data_list[9][23:-2]
sunrise = camera_data_list[10][23:-6]
sunset = camera_data_list[11][23:-6]
elevation = camera_data_list[12][23:-2]
localDate = localDate[0:4] + " " + localDate[5:7] + localDate[8:]

# Grabs your IP address and locates your server location
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
g = geocoder.ip('me')
                
# Sets Longitude and Latitude to string variables which is multplied by 10000 to get a large positive whole nuber
latitude = str(int(g.latlng[0] * 10000))
longitude = str((int(g.latlng[1] * 10000)*-1))
                
# Sets your IP's server city location's length to a variable, in this case San Fransisco is used as our city name
cityLength =  str(len(g.city))

# set all the individual weather data to one string varibable
passwrd = int(latitude + localTime.translate({ord(':'): None}) + cityLength + temperatureHigh + temperatureLow + sunrise.translate({ord(':'): None}) + sunset.translate({ord(':'): None}) + elevation + longitude)

#amount of cars deteceted
amountC = liveScrape.a_of_car_d()

if amountC == 0:
    amountC += 1

#before we get to the best part we have to add a little bit more randomness
passwrd += passwrd + passwrd *amountC

#Shows string variable password
#print( "Password with longitude, latitude, and weather data \n ", passwrd)

# Sends the variable password to the definition above
encoded_password = num_to_alpha(passwrd)

# Shows the new encoded, by base64, password
#print("same Password encoded \n", str(encoded_password)[2:-1])

def ps():
    return str(encoded_password)




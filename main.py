# pip  opencv-python
# opencv-contrib-python
# pip install BeautifulSoup4 pandas selenium
# pip install geopy

import cv2
from bs4 import BeautifulSoup
import requests
import geocoder
import socket
import base64


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
localDate = camera_data_list[0][23:-2]
localTime = camera_data_list[1][23:-6]
temperatureHigh = camera_data_list[8][23:-2]
temperatureLow = camera_data_list[9][23:-2]
sunrise = camera_data_list[10][23:-6]
sunset = camera_data_list[11][23:-6]
elevation = camera_data_list[12][23:-2]
localDate = localDate[0:4] + " " + localDate[5:7] + localDate[8:]

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
g = geocoder.ip('me')
latitude = str(int(g.latlng[0] * 10000))
longitude = str((int(g.latlng[1] * 10000)*-1))
cityLength =  str(len(g.city))

passwrd = int(latitude + localTime.translate({ord(':'): None}) + cityLength + temperatureHigh + temperatureLow + sunrise.translate({ord(':'): None}) + sunset.translate({ord(':'): None}) + elevation + longitude)


print( "Password with longitude, latitude, and weather data \n ", passwrd)
encoded_password = num_to_alpha(passwrd)
print("same Password encoded \n", str(encoded_password)[2:-1])




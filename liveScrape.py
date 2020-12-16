import requests 
import json 
from selenium import webdriver
import urllib

# url containing json file for cctv data 
url = 'https://cwwp2.dot.ca.gov/data/d5/cctv/cctvStatusD05.json'
r = requests.get(url)
data = r.json()


# traverse json to find currentImageURL
for i in data['data']:
    if i['cctv']['index'] == '95': # imjin pwkway 
        new_url = (i['cctv']['imageData']['static']['currentImageURL']) # sets new url to current live feed image
        
# chrome driver to open the url... not necessary to open browser
#driver = webdriver.Chrome(executable_path='/Users/OscarRamirez/Downloads/chromedriver')
#driver.get(new_url)

# saving image to computer
response = requests.get(new_url)
file = open("z.png", "wb")
file.write(response.content)
file.close()
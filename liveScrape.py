import requests 
import json 
from selenium import webdriver # only used to open the browser
import urllib
import cv2 
from matplotlib import pyplot as plt 
import random

# url containing json file for cctv data 
url = 'https://cwwp2.dot.ca.gov/data/d5/cctv/cctvStatusD05.json'
r = requests.get(url)
data = r.json()

# images used are from CalTrans CCTV
# cameras are located by ditricts 
# 122 total districts = 122 total feeds 
# here we make a random generator within this range to choose a location 
index = str(random.randint(1,122))

# traverse json to find currentImageURL
for i in data['data']:
    if i['cctv']['index'] == index: # random index 
        new_url = (i['cctv']['imageData']['static']['currentImageURL']) # sets new url to current live feed image
        
# chrome driver to open the url... not necessary to open browser just an additional feature
#driver = webdriver.Chrome(executable_path='/Users/OscarRamirez/Downloads/chromedriver')
#driver.get(new_url)

# saving image of latest transmission to computer
response = requests.get(new_url)
file = open("z1.png", "wb")
file.write(response.content)
file.close()

# vehicle detection

# best build so far 
# Opens image saved by webScraper
img = cv2.imread("z1.png") 
  
# we need grayscale for imageprocessing but we can use the original with the detection in the final "showing"
grayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
RGBImage = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
  
  
# Use max_size to avoid background objects Hills and such 
car_trained_data = cv2.CascadeClassifier('car2.xml') # trained xml model of car images (didn't have time to build my own so this is the best I could find online)
vehiclesDetected = car_trained_data.detectMultiScale(grayScale, 1.1, 3,minSize= (20,20),maxSize = (100,100))
                                    


# tracker to keep count of how many vehicles are detected based on paramaters from above 
amount_of_vehicles_detected = len(vehiclesDetected) 
# we draw a rectangle around every vehicle detected 
if amount_of_vehicles_detected != 0: 
    for (x, y, w, h) in vehiclesDetected:
        cv2.rectangle(RGBImage, (x, y),  
                      (x + w, y + h),  
                      (0, 255, 0), 1) 

#plots the image if this feature is needed uncomment it 
#plt.subplot(1, 1, 1) 
#plt.imshow(img_rgb) 
#plt.show() 

print(amount_of_vehicles_detected) # amount of vehicles detected

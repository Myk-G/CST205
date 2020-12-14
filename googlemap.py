import gmaps
import geocoder
import socket


# g = geocoder.ip('me')
# latLong = g.latlng
# print(latLong)

gmaps.configure(api_key='AIzaSyBnyQu2Qc0so3HMhq2feR1JaZHrYjMBTjQ')

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

print(local_ip)

# g = geocoder.ip('Monterey, Ca')
# g = geocoder.ip('me')
#
# print(g.latlng)
# print(g.city)

LocalIP = ''.join(socket.gethostbyname_ex(socket.gethostname())[2])

print(LocalIP)

# Imjin_coordinates = (latLong[0], latLong[1])
Imjin_coordinates = (36.668976, -121.812407)
gmaps.figure(center=Imjin_coordinates, zoom_level=12)

print(gmaps.Map)
import phonenumbers
from phonenumbers import timezone,geocoder,carrier
import folium

key = "e07d2a7396bb4a9bbc38f0e6aadff773"

number = input("Enter your no. with +__: ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone, "en")
reg = geocoder.description_for_number(phone, "en")
print(phone)
print(time)
print(car)
print(reg)

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)

query = str(reg)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print( lat , lng )

myMap = folium.Map(location = [lat,lng], zoom_start=9)
folium.Marker([lat,lng], popup=reg).add_to(myMap)
myMap.save("mylocation.html")


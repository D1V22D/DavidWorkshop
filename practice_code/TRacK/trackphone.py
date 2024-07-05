import phonenumbers as ph
from phone import number
from phonenumbers import geocoder as gec
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium as fl

phno = ph.parse(number)
loc = gec.description_for_number(phno,"en")
print(loc)
print(carrier.name_for_number(phno,"en"))



key ='c8dab1ede4004ced9d5f9a1c227663a7'
geocoder = OpenCageGeocode(key)
query = str(loc)
results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng) 

map = fl.Map(location=[lat,lng], zoom_start= 9)
fl.Marker([lat,lng],popup=loc).add_to(map)

map.save("location55.html")
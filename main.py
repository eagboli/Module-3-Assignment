

from flask import Flask, render_template
from get_iss import iss_loc
from get_weather import get_weather
from get_distance import dist
from get_reverse_geo import address
from get_country import country

app = Flask('app')

@app.route('/')
def main():
  data = iss_loc()
  lat,lon = data[0],data[1]
  
  #Weather beneath the ISS
  
  weather = get_weather(lat,lon)
  
  temp_c = round(weather["main"]["temp"] - 273.15,2)
  description = weather["weather"][0]["description"]
  print(str(temp_c)," C", description)
  
  #Reverse geolocation
  add = address (lat,lon)
  
  #Print the country code
  print("Country Code is :", add["countryCode"])
  #name = add["countryName"]
  
  if(add["countryCode"]==""):
    print("The ISS is over water!")
    flag = 'Flag unavailable'
    location = "Water"
    # #this is just to test the one end point(rest countries)
    # location='pe'
    # flag=country(location)[0]["flags"]["png"]
    # print(flag)
  else:
    location = add["countryCode"]
    print(add["countryCode"])
    flag=country(location)[0]["flags"]["png"]
    print(flag)
  
  
  #Distance between ISS and myself (Cambrian College)
  
  distance = dist(lat,lon,46.5290839,-80.9432954)
  
  print(f"I am {distance} km away from the ISS")
  return render_template('index.html', lat=lat, lon=lon, distance=distance, temp_c=temp_c, description=description, location = location, flag=flag)

app.run(host='0.0.0.0', port=8080)
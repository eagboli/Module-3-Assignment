import urllib.request
import json

def iss_loc():
  url='http://api.open-notify.org/iss-now.json'
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())
  
  #print(result)
  
  #Pass the latitude and longitude to this end point to google map.
  
  lat = result["iss_position"]["latitude"]
  lon = result["iss_position"]["longitude"]
  
  print("Google Map","https://www.google.ca/maps/place/"+lat +"+" + lon)
  return lat,lon
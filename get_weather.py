import urllib.request
import json


def get_weather(lat,lon):
  key= 'bc448800d4c0db057fde7aafc4a36d6d'
  
  url= f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}'
  
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())

  return result


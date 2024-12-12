import urllib.request
import json

def address(lat,lon):
  key = 'bdc_386b209435e747ceae90e5f669b31876'
  url=f'https://api-bdc.net/data/reverse-geocode?latitude={lat}&longitude={lon}&localityLanguage=en&key={key}'
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())
  return result

import json
from urllib.request import urlopen
#Create user account and obtain API key from https://www.weatherapi.com

url = "https://api.weatherapi.com/v1/current.json?key=f4a34d94e01244fe92f32019232905&q=kollam&aqi=no"

api_page = urlopen(url)
api=api_page.read()
json_api=json.loads(api)
# data= json_api['currently']
#print(data)
print(json_api)

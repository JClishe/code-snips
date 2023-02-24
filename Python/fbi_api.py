import requests
import json

response = requests.get('https://api.fbi.gov/wanted/v1/list')
data = json.loads(response.content)
print(data['total'])
#print(data['items'][10]['title'])
print(data['items'][10])
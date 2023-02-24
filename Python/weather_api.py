import requests
import json

response = requests.get('https://api.weather.gov')
alerts = requests.get('https://api.weather.gov/alerts/active?area=OH')
data = json.loads(response.content)
print(alerts)
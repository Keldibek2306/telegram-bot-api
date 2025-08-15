import requests
from settings import TOKEN


BASE_URL = f'https://api.telegram.org/bot{TOKEN}'

getupdates_url = f'{BASE_URL}/getUpdates'
response = requests.get(getupdates_url)

print(response.json())
import requests
from settings import TOKEN


BASE_URL = f'https://api.telegram.org/bot{TOKEN}'

getme_url = f'{BASE_URL}/getMe'
response = requests.get(getme_url)

print(response.json())
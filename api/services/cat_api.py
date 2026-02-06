import requests

URL = 'https://api.thecatapi.com/v1/images/search'

def cat_image():
    response = requests.get(URL, timeout=5)
    response.raise_for_status()
    data=response.json()
    return data
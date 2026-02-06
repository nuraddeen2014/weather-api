import requests


URL = 'https://api.adviceslip.com/advice'

def advice_api():
    response = requests.get(url=URL, timeout=5)
    response.raise_for_status()
    return response.json()
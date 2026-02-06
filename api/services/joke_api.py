import requests


URL = 'https://official-joke-api.appspot.com/random_joke'

def joke_api():
    response = requests.get(URL)
    response.raise_for_status()
    return response.json()
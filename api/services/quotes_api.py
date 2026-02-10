import requests


URL ='https://zenquotes.io/api/random'

def quotes_api():
    response = requests.get(URL, timeout=5)
    response.raise_for_status()
    return response.json()
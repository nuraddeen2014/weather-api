import requests


URL = 'https://api.agify.io/'

def age_prediction_api(name):
    params = {'name':name}

    response = requests.get(url=URL, params=params, timeout=5)
    response.raise_for_status()
    return response.json()

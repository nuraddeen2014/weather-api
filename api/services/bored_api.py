import requests


URL = 'https://bored-api.appbrewery.com/filter'


def bored_api(activity_type):
    response = requests.get(URL, timeout=5, params={'type':activity_type})
    response.raise_for_status()
    return response.json()
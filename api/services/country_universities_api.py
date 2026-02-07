import requests

URL = 'http://universities.hipolabs.com/search'


def country_universities_api(country):
    response = requests.get(url=URL, params={'country':country}, timeout=5)
    response.raise_for_status()
    return response.json()
import requests

BASE_URL = 'https://restcountries.com/v3.1/name/'


def country_data(country):
    url = f'{BASE_URL}{country}'
    response = requests.get(url, timeout=5)
    response.raise_for_status()

    data = response.json()
    return data


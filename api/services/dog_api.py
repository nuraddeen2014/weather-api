import requests

url = "https://dog.ceo/api/breeds/image/random"

def dog_api():
    
    response = requests.get(url, timeout=5)
    data = response.json()
    response.raise_for_status()
    return data['message']

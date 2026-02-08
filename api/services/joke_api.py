"""
Joke API Service Module

This module provides functionality to fetch random jokes from the Official Joke API.
It retrieves jokes in a setup/punchline format for entertainment purposes.
"""

import requests

# Official Joke API endpoint for fetching random jokes
URL = 'https://official-joke-api.appspot.com/random_joke'

def joke_api():
    """
    Fetches a random joke from the Official Joke API.
    
    This function makes an HTTP GET request to the Official Joke API and retrieves
    a random joke in setup/punchline format.
    
    Returns:
        dict: A dictionary containing joke data with keys:
              - 'setup': The setup/premise of the joke (str)
              - 'punchline': The punchline/conclusion of the joke (str)
              - 'type': The category of the joke (str)
              - 'id': Unique identifier for the joke (int)
    
    Raises:
        requests.exceptions.RequestException: If the HTTP request fails.
        json.JSONDecodeError: If the response is not valid JSON.
    
    Example:
        >>> joke = joke_api()
        >>> print(f"{joke['setup']} {joke['punchline']}")
    """
    response = requests.get(URL)
    response.raise_for_status()
    return response.json()
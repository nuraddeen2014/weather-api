"""
Advice API Service Module

This module provides functionality to fetch random life advice from the Advice Slip API.
It serves as an integration point for retrieving daily wisdom and motivational quotes.
"""

import requests

# Advice Slip API endpoint for fetching random advice
URL = 'https://api.adviceslip.com/advice'

def advice_api():
    """
    Fetches random life advice from the Advice Slip API.
    
    This function makes an HTTP GET request to the Advice Slip API and retrieves
    a random piece of advice or wisdom.
    
    Returns:
        dict: A dictionary containing advice data with a 'slip' key containing:
              - 'advice': The advice/wisdom text (str)
              - 'slip_id': Unique identifier for the advice (int)
    
    Raises:
        requests.exceptions.RequestException: If the HTTP request fails or times out.
        json.JSONDecodeError: If the response is not valid JSON.
    
    Example:
        >>> advice = advice_api()
        >>> print(advice['slip']['advice'])
    """
    response = requests.get(url=URL, timeout=5)
    response.raise_for_status()
    return response.json()
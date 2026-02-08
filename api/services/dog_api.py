"""
Dog API Service Module

This module provides functionality to fetch random dog images from the Dog CEO API.
It serves as an external API integration for retrieving cute dog photos.
"""

import requests

# Dog CEO API endpoint for fetching random dog images
url = "https://dog.ceo/api/breeds/image/random"

def dog_api():
    """
    Fetches a random dog image URL from the Dog CEO API.
    
    This function makes an HTTP GET request to the Dog CEO API and retrieves
    a random dog image. The API returns a JSON response containing the image URL.
    
    Returns:
        str: A URL string pointing to a random dog image.
    
    Raises:
        requests.exceptions.RequestException: If the HTTP request fails or times out.
        json.JSONDecodeError: If the response is not valid JSON.
    
    Example:
        >>> image_url = dog_api()
        >>> print(image_url)
        'https://images.dog.ceo/breeds/...'
    """
    response = requests.get(url, timeout=5)
    data = response.json()
    response.raise_for_status()
    return data['message']

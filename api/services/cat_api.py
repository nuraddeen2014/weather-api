"""
Cat API Service Module

This module provides functionality to fetch random cat images from The Cat API.
It integrates with an external API service to retrieve cat photos with metadata.
"""

import requests

# The Cat API endpoint for searching and retrieving cat images
URL = 'https://api.thecatapi.com/v1/images/search'

def cat_image():
    """
    Fetches a random cat image from The Cat API.
    
    This function makes an HTTP GET request to The Cat API and retrieves
    cat image data including the image URL and dimensions (width, height).
    
    Returns:
        list: A list containing dictionaries with cat image data. Each dictionary
              contains keys like 'url', 'width', and 'height'.
    
    Raises:
        requests.exceptions.RequestException: If the HTTP request fails or times out.
        json.JSONDecodeError: If the response is not valid JSON.
    
    Example:
        >>> images = cat_image()
        >>> print(images[0]['url'])
        'https://cdn2.thecatapi.com/images/...'
    """
    response = requests.get(URL, timeout=5)
    response.raise_for_status()
    data=response.json()
    return data
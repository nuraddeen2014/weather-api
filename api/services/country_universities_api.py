"""
Country Universities API Service Module

This module provides functionality to fetch university information for a given country.
It integrates with the Hipolabs Universities API to retrieve a list of universities
and their associated information for any specified country.
"""

import requests

# Hipolabs Universities API endpoint for searching universities by country
URL = 'http://universities.hipolabs.com/search'

def country_universities_api(country):
    """
    Fetches a list of universities in a specified country.
    
    This function makes an HTTP GET request to the Hipolabs Universities API and
    retrieves all universities registered for the given country.
    
    Args:
        country (str): The name of the country to search for universities (e.g., 'United States', 'Japan').
    
    Returns:
        list: A list of dictionaries containing university data. Each dictionary includes keys:
              - 'name': University name (str)
              - 'country': Country name (str)
              - 'web_pages': List of university website URLs (list of str)
              - 'domains': Academic domain names (list of str)
              - 'alpha_two_code': ISO 3166-1 alpha-2 country code (str)
    
    Raises:
        requests.exceptions.RequestException: If the HTTP request fails or times out.
        json.JSONDecodeError: If the response is not valid JSON.
    
    Example:
        >>> universities = country_universities_api('Germany')
        >>> print(universities[0]['name'])
        'Example University'
    """
    response = requests.get(url=URL, params={'country':country}, timeout=5)
    response.raise_for_status()
    return response.json()
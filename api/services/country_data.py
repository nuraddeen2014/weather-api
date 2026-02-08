"""
Country Data API Service Module

This module provides functionality to fetch detailed information about countries.
It uses the REST Countries API to retrieve comprehensive country data including
capital, population, region, flag emoji, and other geographical information.
"""

import requests

# REST Countries API base URL for fetching country information by name
BASE_URL = 'https://restcountries.com/v3.1/name/'

def country_data(country):
    """
    Fetches detailed information about a country from the REST Countries API.
    
    This function makes an HTTP GET request to the REST Countries API and retrieves
    comprehensive data about a specified country. The country name is used to search
    and retrieve matching country records.
    
    Args:
        country (str): The name of the country to fetch data for (e.g., 'United States', 'France').
    
    Returns:
        list: A list of dictionaries containing country data. Each dictionary includes keys such as:
              - 'name': Dictionary with common and official names (dict)
              - 'capital': List of capital cities (list)
              - 'population': Population count (int)
              - 'region': Continental region (str)
              - 'flag': Flag emoji character (str)
              - 'area': Land area in square kilometers (float)
              - 'currencies': Available currencies (dict)
              - And many other geographical and political details
    
    Raises:
        requests.exceptions.RequestException: If the HTTP request fails or times out.
        json.JSONDecodeError: If the response is not valid JSON.
    
    Example:
        >>> country_info = country_data('Italy')
        >>> print(country_info[0]['name']['common'])
        'Italy'
    """
    url = f'{BASE_URL}{country}'
    response = requests.get(url, timeout=5)
    response.raise_for_status()

    data = response.json()
    return data


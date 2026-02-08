"""
Age Prediction API Service Module

This module provides functionality to predict a person's age based on their name.
It uses the Agify.io API to estimate age demographics for given names.
"""

import requests

# Agify.io API endpoint for predicting age based on name
URL = 'https://api.agify.io/'

def age_prediction_api(name):
    """
    Predicts the age of a person based on their name using the Agify.io API.
    
    This function makes an HTTP GET request to the Agify.io API with a given name
    and returns the predicted age based on statistical analysis of the name.
    
    Args:
        name (str): The person's name for which to predict the age.
    
    Returns:
        dict: A dictionary containing age prediction data with keys:
              - 'name': The name provided (str)
              - 'age': The predicted age (int or None if prediction unavailable)
              - 'count': The count of data points used for prediction (int)
    
    Raises:
        requests.exceptions.RequestException: If the HTTP request fails or times out.
        json.JSONDecodeError: If the response is not valid JSON.
    
    Example:
        >>> prediction = age_prediction_api('Michael')
        >>> print(f"Predicted age for Michael: {prediction['age']}")
    """
    params = {'name':name}

    response = requests.get(url=URL, params=params, timeout=5)
    response.raise_for_status()
    return response.json()

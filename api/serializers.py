"""
Serializers Module

This module contains Django REST Framework serializers used for request validation
and response formatting. Serializers ensure data integrity by validating input
parameters and structuring output responses.

Serializers included:
- CountryDetailSerializer: Validates and formats country information
- CountryQuerySerializer: Validates country name query parameter
- AgeQuerySerializer: Validates name query parameter for age prediction
- CountryUniversitiesQuerySerializer: Validates country query parameter for universities
- UniversitySerializer: Formats individual university data
- CountryUniversitiesSerializer: Combines country data with list of universities
"""

from rest_framework import serializers


class CountryDetailSerializer(serializers.Serializer):
    """
    Serializer for country detail information.
    
    This serializer validates and formats detailed country data returned from the
    REST Countries API. It ensures all required fields are present and properly typed.
    
    Fields:
        - name (str): Country name (common name)
        - capital (str): Capital city name
        - population (int): Total population count
        - flag (str): Flag emoji character
        - region (str): Continental region (e.g., 'Europe', 'Asia')
    
    Usage:
        data = {
            'name': 'France',
            'capital': 'Paris',
            'population': 67750000,
            'flag': '🇫🇷',
            'region': 'Europe'
        }
        serializer = CountryDetailSerializer(data=data)
        if serializer.is_valid():
            return serializer.data
    """
    name = serializers.CharField()
    capital = serializers.CharField()
    population = serializers.IntegerField()
    flag = serializers.CharField()
    region = serializers.CharField()


class CountryQuerySerializer(serializers.Serializer):
    """
    Serializer for validating country name query parameters.
    
    This serializer validates input query parameters for endpoints that accept
    a country name. It ensures the 'name' parameter is provided and is a valid string.
    
    Fields:
        - name (str, required): The name of the country to query
    
    Usage:
        serializer = CountryQuerySerializer(data=request.query_params)
        if serializer.is_valid(raise_exception=True):
            country_name = serializer.validated_data['name']
            # Process country_name
    """
    name = serializers.CharField(required=True)


class AgeQuerySerializer(serializers.Serializer):
    """
    Serializer for validating age prediction query parameters.
    
    This serializer validates input query parameters for age prediction endpoints.
    It ensures the 'name' parameter is provided and is a valid string.
    
    Fields:
        - name (str, required): The person's name for age prediction
    
    Usage:
        serializer = AgeQuerySerializer(data=request.query_params)
        if serializer.is_valid(raise_exception=True):
            name = serializer.validated_data['name']
            # Predict age for name
    """
    name = serializers.CharField(required=True)


class CountryUniversitiesQuerySerializer(serializers.Serializer):
    """
    Serializer for validating country name query parameters for universities endpoint.
    
    This serializer validates input query parameters for university-related endpoints.
    It ensures the 'country' parameter is provided with a minimum length requirement.
    
    Fields:
        - country (str, required, min_length=1): The name of the country to search for universities
    
    Usage:
        serializer = CountryUniversitiesQuerySerializer(data=request.query_params)
        if serializer.is_valid(raise_exception=True):
            country = serializer.validated_data['country']
            # Fetch universities for country
    """
    country = serializers.CharField(min_length=1,required=True)


class UniversitySerializer(serializers.Serializer):
    """
    Serializer for formatting individual university data.
    
    This serializer formats university information from the Hipolabs Universities API.
    It extracts the university name and first website URL (converted from the web_pages list).
    
    Fields:
        - name (str): University name
        - website (str): Primary website URL (extracted from web_pages list via SerializerMethodField)
    
    The get_website method is a SerializerMethodField that extracts the first (primary)
    website from the university's web_pages list.
    
    Usage:
        universities_data = [{'name': 'MIT', 'web_pages': ['http://mit.edu', ...], ...}]
        serializer = UniversitySerializer(universities_data, many=True)
        return serializer.data
    """
    name = serializers.CharField()
    website = serializers.SerializerMethodField()

    def get_website(self, obj):
        """
        Extract the first website URL from the university's web_pages list.
        
        Args:
            obj (dict): University object containing 'web_pages' list
        
        Returns:
            str: The first (primary) website URL
        """
        return obj['web_pages'][0]


class CountryUniversitiesSerializer(serializers.Serializer):
    """
    Serializer for formatting country and its universities data.
    
    This serializer combines country information with a list of universities.
    It uses a custom to_representation method to structure the response properly,
    extracting the country name from the first university record and formatting
    all universities using UniversitySerializer.
    
    Fields:
        - country (str): Country name
        - universities (list): List of university objects formatted by UniversitySerializer
    
    The to_representation method is overridden to:
    1. Extract the country name from the first item in the list (all items have same country)
    2. Format all universities using UniversitySerializer
    3. Return a properly structured response
    
    Usage:
        universities_list = [  # List of university dicts from API
            {'name': 'MIT', 'country': 'United States', 'web_pages': [...], ...},
            {'name': 'Harvard', 'country': 'United States', 'web_pages': [...], ...}
        ]
        serializer = CountryUniversitiesSerializer(instance=universities_list)
        return serializer.data
    
    Returns:
        dict: Structured response with:
            {
                'country': 'United States',
                'universities': [
                    {'name': 'MIT', 'website': 'http://...'},
                    {'name': 'Harvard', 'website': 'http://...'}
                ]
            }
    """
    country =serializers.CharField()
    universities = UniversitySerializer(many=True)

    def to_representation(self, instance):
        """
        Custom representation to format university list with country information.
        
        Args:
            instance (list): List of university dictionaries from the API
        
        Returns:
            dict: Formatted response with country name and formatted universities list
        """
        country = instance[0].get('country')

        universities = UniversitySerializer(instance, many=True).data
        
        return {
            'country':country,
            'universities':universities
        }
    
class BoredQuerySerializer(serializers.Serializer):
    type = serializers.CharField(required=True, min_length=1)
    
class BoredSerialier(serializers.Serializer):
    activity = serializers.CharField()
    type = serializers.CharField()
    participants = serializers.IntegerField()

class QuotesSerializer(serializers.Serializer):
    quote = serializers.CharField()
    author = serializers.CharField()

    def to_representation(self, instance):
        
        quote = instance['q']
        author = instance['a']

        return {
            'quote':quote,
            'author':author
        }
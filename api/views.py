import requests
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .services.dog_api import dog_api
from .services.country_data import country_data
from .services.cat_api import cat_image
from .services.advice_api import advice_api
from .services.joke_api import joke_api
from.services.age_prediction_api import age_prediction_api
from.services.country_universities_api import country_universities_api
from .serializers import CountryDetailSerializer, CountryQuerySerializer, AgeQuerySerializer, CountryUniversitiesQuerySerializer,CountryUniversitiesSerializer
import json

# Create your views here.
@api_view(['GET'])
def random_dog(request):
    try:
        image_url = dog_api()
        return Response({'image_url':image_url}, status=status.HTTP_200_OK)
    except Exception:
        return Response({'error':'Failed to fetch Dog'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
    
@api_view(['GET'])
def get_country_data(request):
    query = CountryQuerySerializer(data=request.query_params)
    query.is_valid(raise_exception=True)

    country_name = query.validated_data['name']
    
    try:
        country_info = country_data(country_name)

        data = {
            'name':country_info[0]['name']['common'],
            'capital': country_info[0]['capital'][0],
            'population': country_info[0]['population'],
            'flag': country_info[0]['flag'],
            'region': country_info[0]['region']
        }
        serializer = CountryDetailSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    except Exception:
        return Response({'error':'Failed to fetch data'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
    
@api_view(['GET'])
def get_cat_image(request):
    try:
        image = cat_image()[0]
        image_data = {
            'image_url':image['url'],
            'width':image['width'],
            'height':image['height'],
        }
        return Response(data=image_data, status=status.HTTP_200_OK)
    except requests.exceptions.RequestException:
        return Response({'errror':'Error fetching url'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
    
@api_view(['GET'])
def get_random_joke(request):
    try:
        joke = joke_api()
        joke_data = {
            'setup':joke['setup'],
            'punchline':joke['punchline']
            }
        return Response(data=joke_data, status=status.HTTP_200_OK)
    
    except requests.exceptions.RequestException:
        return Response({'error':'Error fetching joke'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
    
@api_view(['GET'])
def get_random_advice(request):
    try:
        advice = advice_api()
        advice_data = {
            'advice':advice['slip']['advice']
        }
        return Response(data=advice_data, status=status.HTTP_200_OK)
    
    except requests.exceptions.RequestException:
        return Response({'error':'Failed to fetch advice'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
    
@api_view(['GET'])
def get_age_prediction(request):
    query = AgeQuerySerializer(data=request.query_params)
    query.is_valid(raise_exception=True)
    name = query.validated_data['name']

    try:
        age_prediction = age_prediction_api(name)
        age_prediction_data = {
            'name': age_prediction['name'],
            'predicted_age': age_prediction.get('age')
        }
        return Response(data=age_prediction_data, status=status.HTTP_200_OK)
    
    except requests.exceptions.RequestException:
        return Response({'error':'Fetching age data failed.'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
    
@api_view(['GET'])
def get_country_universities(request):
    query = CountryUniversitiesQuerySerializer(data=request.query_params)
    query.is_valid(raise_exception=True)
    country = query.validated_data['country']

    try:
        country_universities = country_universities_api(country=country)

        data_list = []
        for i in  country_universities:
            
            data_dict = {
                'name': i['name'],
                'website': i['web_pages'][0]
                }
            
            data_list.append(data_dict)
        data = {
                'country': country_universities[0]['country'],
                'universities': data_list
            }

        
        return Response(data=data, status=status.HTTP_200_OK)
    except requests.exceptions.RequestException:
        return Response({'error':'Failed to fetch data'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

@api_view(['GET'])
def get_pro_country_universities(request):
    query = CountryUniversitiesQuerySerializer(data=request.query_params)
    query.is_valid(raise_exception=True)
    country = query.validated_data['country']

    try:
        country_universities = country_universities_api(country=country)

        data = {
            'country': country,
            'universities': country_universities
        }

        serializer = CountryUniversitiesSerializer(instance=data)
        

        
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    except requests.exceptions.RequestException:
        return Response({'error':'Failed to fetch data'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
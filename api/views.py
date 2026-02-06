import requests
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .services.dog_api import dog_api
from .services.country_data import country_data

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
    country_name = request.query_params.get('name')
    try:
        if not country_name:
            return Response({'error':'name cannnot be empty'}, status=status.HTTP_400_BAD_REQUEST)
        
        country_info = country_data(country_name)

        data = {
            'name':country_info[0]['name']['common'],
            'capital': country_info[0]['capital'][0],
            'population': country_info[0]['population'],
            'flag': country_info[0]['flag'],
            'region': country_info[0]['region']
        }
        return Response(data, status=status.HTTP_200_OK)
    
    except Exception:
        return Response({'error':'Failed to fetch data'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
    

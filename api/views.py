import requests
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .services.dog_api import dog_api

# Create your views here.
@api_view(['GET'])
def random_dog(request):
    try:
        image_url = dog_api()
        return Response({'image_url':image_url}, status=status.HTTP_200_OK)
    except Exception:
        return Response({'error':'Failed to fetch Dog'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
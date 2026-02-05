import requests
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def dog_api(request):
    url = "https://dog.ceo/api/breeds/image/random"
    r = requests.get(url, timeout=1)
    
    if r.status_code == requests.codes.ok:
        data = {'data':r.json()}
        return Response(data, status=status.HTTP_200_OK)
    
    return Response(r.raise_for_status())

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dog_api)
]
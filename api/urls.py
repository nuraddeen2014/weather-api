from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.random_dog)
]
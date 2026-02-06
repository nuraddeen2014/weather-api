from django.urls import path, include
from . import views

urlpatterns = [
    path('dog/', views.random_dog),
    path('country/', views.get_country_data)
]
from django.urls import path, include
from . import views

urlpatterns = [
    path('dog/', views.random_dog),
    path('cat/', views.get_cat_image),
    path('joke/', views.get_random_joke),
    path('advice/', views.get_random_advice),
    path('age/', views.get_age_prediction),
    path('universities/', views.get_country_universities),
    path('universities/pro/', views.get_pro_country_universities),
    path('bored/', views.get_boredom_advice),
    path('country/', views.get_country_data)
]
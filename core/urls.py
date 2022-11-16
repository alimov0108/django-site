from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('about/', about),
    path('tesla/', tesla),
    path('chevrolet/', chevrolet),
    path('ferrari/', ferrari),
    path('kamaro/', kamaro),
    path('lamborgini/', lamborgini),
    path('wolksvagen/', wolksvagen),
    path('mustang/', mustang),
]

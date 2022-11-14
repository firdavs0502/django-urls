from django.urls import path
from .views import *

urlpatterns = [
    path('chevrolet/', chevrolet),
    path('chevrolet2/', chevrolet2),
    path('chevrolet3/', chevrolet3),
]

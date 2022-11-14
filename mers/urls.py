from django.urls import path
from .views import *

urlpatterns = [
    path('mers/', mers),
    path('mers2/', mers2),
    path('mers3/', mers3),
]

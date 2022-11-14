from django.urls import path
from .views import *

urlpatterns = [
    path('bmw/', bmw),
    path('bmw2/', bmw2),
    path('bmw3/', bmw3),
]

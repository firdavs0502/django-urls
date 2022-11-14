from django.shortcuts import render

# Create your views here.


def bmw(request):
    return render(request, 'bmw.html')

def bmw2(request):
    return render(request, 'bmw2.html')

def bmw3(request):
    return render(request, 'bmw3.html')
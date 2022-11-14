from django.shortcuts import render

# Create your views here.

def mers(request):
    return render(request, 'mers.html')

def mers2(request):
    return render(request, 'mers2.html')

def mers3(request):
    return render(request, 'mers3.html')
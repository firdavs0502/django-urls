from django.shortcuts import render

# Create your views here.


def chevrolet(request):
    return render(request, 'chevrolet.html')

def chevrolet2(request):
    return render(request, 'chevrolet2.html')

def chevrolet3(request):
    return render(request, 'chevrolet3.html')

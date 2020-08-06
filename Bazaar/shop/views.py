from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.

def index(request):
    products = Product.objects.all() 
    n = len(products)
    nSlides = n//4 + ceil((n/4) - (n//4))
    param = {
        'product': products
    }
    return render(request, 'shop/index.html', param)
    
def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse("c")

def tracker(request):
    return HttpResponse("r")

def productView(request):
    return HttpResponse("p")

def search(request):
    return HttpResponse("s")

def checkout(request):
    return HttpResponse("c")

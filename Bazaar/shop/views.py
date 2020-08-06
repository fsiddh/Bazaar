from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.

def index(request):
    product = Product.objects.all() 
    data = {
        'Product': product
    }
    return render(request, 'shop/index.html', data)
    
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

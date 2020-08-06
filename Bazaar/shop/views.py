from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'shop/index.html')
    
def about(request):
    return HttpResponse("a")

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

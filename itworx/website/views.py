from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product

def Home(request):
    return render(request,"website/Home.html",
                  {"products" : Product.objects.all()})

def Products(request):
    return render(request, "website/products.html",
                  {"products": Product.objects.all()})

def Date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))

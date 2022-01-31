from django.shortcuts import render
from django.db import models


# Create your views here.

def index(request):
    return render(request, "index.html")


def home(request):
    return render(request, 'makeup/index.html')


def brands(request):

    return render(request, "makeup/brands.html")


def products(request):
    return render(request, "makeup/products.html")


def brand_details(request):
    return render(request, "makeup/brand_details.html")


def product_details(request):
    return render(request, "makeup/product_details.html")

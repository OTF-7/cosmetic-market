from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Brand, Product


# Create your views here.

def home(request):
    brands = Brand.objects.all()
    products = Product.objects.all()
    context = {
        "brands": brands,
        "products": products
    }
    return render(request, "makeup/index.html", context)


# def brands(request):
#     return render(request, "makeup/brands.html")
#
#
# def products(request):
#     return render(request, "makeup/products.html")


class ProductDetailsView(DetailView):
    model = Product
    template_name = 'makeup/product_details.html'


class ProductListView(ListView):
    model = Product
    template_name = 'makeup/products.html'


class BrandDetailsView(DetailView):
    model = Brand
    template_name = 'makeup/brand_details.html'


class BrandListView(ListView):
    model = Brand
    template_name = 'makeup/brands.html'

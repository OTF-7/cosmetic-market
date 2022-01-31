from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("brands/", views.brands, name="brands"),
    path("products/", views.products, name="products"),
    path("brand_details/", views.brand_details, name="brand_details"),
    path("product_details/", views.product_details, name="product_details"),
]
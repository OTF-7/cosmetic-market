from django.urls import path

from makeup.views import *

urlpatterns = [
    path("", home, name="home"),
    path("brands/", BrandListView.as_view(), name="brands"),
    path("products/", ProductListView.as_view(), name="products"),
    path("brands/brand_details/<slug:slug>", BrandDetailsView.as_view(), name="brand_details"),
    path("products/product_details/<slug:slug>", ProductDetailsView.as_view(), name="product_details"),
]

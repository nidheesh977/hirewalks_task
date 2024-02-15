from django.urls import path 
from . import views

app_name = "seller"

urlpatterns = [
    path("product-list/", views.SellerProductList.as_view(), name = "seller_products")
]
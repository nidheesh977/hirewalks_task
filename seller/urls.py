from django.urls import path 
from . import views

app_name = "seller"

urlpatterns = [
    path("product-list/", views.SellerProductList.as_view(), name = "seller_products"),
    path("buyer-list/<str:product_id>/", views.BuyersList.as_view(), name = "buyers_list"),
]
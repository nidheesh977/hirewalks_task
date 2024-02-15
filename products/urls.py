from django.urls import path 
from . import views

app_name = "products"

urlpatterns = [
    path("", views.CategoriesListView.as_view(), name = "homepage"),
    path("category-<str:id>/", views.ProductListView.as_view(), name = "category_products"),
    path("product-<str:id>/color-<str:color_id>", views.ProductLandingView.as_view(), name = "product_landing"),
]
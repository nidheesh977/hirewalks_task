from django.shortcuts import render, redirect
from django.views import View
from .models import Product, ProductCategory, Color
from orders.models import Cart
# Create your views here.

class CategoriesListView(View):
    def get(self, request):
        search = request.GET.get("search")
        if not search:
            search = ""
        product_categories = ProductCategory.objects.filter(title__icontains = search)
        context = {"product_categories": product_categories}
        return render(request, "products/index.html", context=context)

class ProductListView(View):
    def get(self, request, *args, **kwargs):
        print(kwargs["id"])
        search = request.GET.get("search")
        if not search:
            search = ""
        category = ProductCategory.objects.get(id = kwargs["id"])
        products = Product.objects.filter(title__icontains = search, product_category = category)
        category_title = category.title
        context = {"products": products, "category_title": category_title}
        return render(request, "products/category_products.html", context=context)

class ProductLandingView(View):
    def get(self, request, *args, **kwargs):
        product = Product.objects.get(id = kwargs["id"])
        selected_color = Color.objects.get(id = kwargs["color_id"])
        context = {"product": product, "selected_color": selected_color}
        return render(request, "products/product_details.html", context = context)

    def post(self, request, *args, **kwargs):
        product = Product.objects.get(id = kwargs["id"])
        selected_color = Color.objects.get(id = kwargs["color_id"])
        print(product)
        if request.user.is_authenticated:
            if Cart.objects.filter(buyer = request.user, product = product, color = selected_color).exists():
                cart = Cart.objects.filter(buyer = request.user, product = product, color = selected_color).first()
                cart.count = cart.count+1
                cart.save()
            else:
                Cart.objects.create(
                    buyer = request.user,
                    product = product,
                    color = selected_color,
                    count = 1
                )
            return redirect("orders:cart")
        else:
            return redirect("accounts:login")
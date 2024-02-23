from django.shortcuts import render
from django.views import View 
from products.models import Product
from orders.models import Orders

# Create your views here.

class SellerProductList(View):
    def get(self, request):
        products = Product.objects.all()
        context = {"products": products}
        return render(request, "seller/product_list.html", context)

class BuyersList(View):
    def get(self, request, *args, **kwargs):
        product = Product.objects.get(id = kwargs["product_id"])
        orders = Orders.objects.filter(product = product)

        return render(request, 'seller/buyer_list.html', context = {"buyers": orders})
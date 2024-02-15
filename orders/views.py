from django.shortcuts import render, redirect
from accounts.models import Address
from accounts.forms import AddressForm
from django.views import View
from .models import Cart, Orders
# Create your views here.

class AddressView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if Address.objects.filter(buyer = request.user).exists():
                address = Address.objects.filter(buyer = request.user).order_by("-id").first()
                initial_values = {
                    "title": address.title,
                    "fullName": address.fullName,
                    "addressLine1": address.addressLine1,
                    "addressLine2": address.addressLine2,
                    "city": address.city,
                    "state": address.state,
                    "pincode": address.pincode,
                    "country": address.country,
                    "mobile": address.mobile
                }
            else:
                initial_values = {}
            form = AddressForm(initial = initial_values)
            context = {"form": form}
            return render(request, "orders/address.html", context = context)
        
        return redirect("accounts:login")

    def post(self, request, *args, **kwargs):
        address = Address.objects.create(
            title = request.POST["title"],
            buyer = request.user,
            fullName = request.POST["fullName"],
            addressLine1 = request.POST["addressLine1"],
            addressLine2 = request.POST["addressLine2"],
            city = request.POST["city"],
            state = request.POST["state"],
            pincode = request.POST["pincode"],
            country = request.POST["country"],
            mobile = request.POST["mobile"],
        )
        carts = Cart.objects.filter(buyer = request.user)
        for cart in carts:
            order = Orders.objects.create(
                buyer = request.user,
                product = cart.product,
                color = cart.color,
                address = address,
                count = cart.count,
                price = cart.total_price,
            )
        
        carts.delete()

        return redirect("orders:orders_list")
    
class CartView(View):
    def get(self, request):
        if request.user.is_authenticated:
            carts = Cart.objects.filter(buyer = request.user).order_by("-id")
            cart_total = 0
            for cart in carts:
                cart_total+=int(cart.total_price)
            context = {"carts": carts, "cart_total": cart_total}
            return render(request, "orders/cart.html", context = context)
        return redirect("accounts:login")
    def post(self, request):
        cart = Cart.objects.get(id = request.POST["cart_id"])
        if request.POST["action"] == "add":
            cart.count = cart.count+1
        else:
            cart.count = cart.count-1
        cart.save()

        if cart.count == 0:
            cart.delete()

        return redirect("orders:cart")
class OrdersView(View):
    def get(self, request):
        if request.user.is_authenticated:
            orders = Orders.objects.filter(buyer = request.user).order_by("-id")
            context = {'orders': orders}
            return render(request, "orders/orders.html", context = context)
        return redirect("accounts:login")
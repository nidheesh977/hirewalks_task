from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("products.urls", "products")),
    path('accounts/', include("accounts.urls", "accounts")),
    path('cart-order/', include("orders.urls", "orders")),
    path('seller/', include("seller.urls", "seller")),
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {"document_root": settings.STATIC_ROOT}),
]
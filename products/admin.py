from django.contrib import admin
from .models import Image, Color, ProductCategory, Product, Specification

# Register your models here.
admin.site.register(Image)
admin.site.register(Color)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Specification)
from django.db import models
from colorfield.fields import ColorField
from accounts.models import CustomUser

# Create your models here.
    
class Image(models.Model):
    image = models.ImageField(upload_to = "product_images")

class Color(models.Model):
    color = ColorField(default='#FF0000')
    main_image = models.ForeignKey(Image, on_delete = models.CASCADE, related_name = "main_image")
    sub_images = models.ManyToManyField(Image, related_name = "sub_images")
    count = models.IntegerField()

class ProductCategory(models.Model):
    class Meta:
        verbose_name_plural = "Product Categories"
    title = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.title
    
class Specification(models.Model):
    key = models.CharField(max_length = 200)
    value = models.CharField(max_length = 200)

    def __str__(self):
        return f"{self.key} - {self.value}"
    
class Product(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    product_category = models.ForeignKey(ProductCategory, on_delete = models.CASCADE)
    price = models.IntegerField()
    colors = models.ManyToManyField(Color)
    specifications = models.ManyToManyField(Specification, blank = True)
    color_required = models.BooleanField(default = True)
    seller = models.ForeignKey(CustomUser, on_delete = models.CASCADE)

    @property
    def count(self):
        all_colors = self.colors.all()
        total_count = 0
        for color in all_colors:
            total_count+=color.count

        return total_count

    def __str__(self):
        return self.title
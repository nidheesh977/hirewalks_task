from django.db import models
from accounts.models import CustomUser, Address
from products.models import Product, Color

# Create your models here.
class Cart(models.Model):
    buyer = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    color = models.ForeignKey(Color, on_delete = models.CASCADE)
    count = models.IntegerField(default = 1)

    @property
    def total_price(self):
        return str(self.product.price*self.count)

    def __str__(self):
        return self.product.title
    
class Orders(models.Model):
    class Meta:
        verbose_name_plural = "Orders"
    DELIVERY_STATUS = (
        ("pending", "Pending"),
        ("packed", "Packed"),
        ("on_the_way", "On the way"),
        ("out_for_delivery", "Out for delivery")
    )
    buyer = models.ForeignKey(CustomUser, on_delete = models.PROTECT)
    product = models.ForeignKey(Product, on_delete = models.PROTECT)
    color = models.ForeignKey(Color, on_delete = models.PROTECT)
    address = models.ForeignKey(Address, on_delete = models.PROTECT)
    count = models.IntegerField(default = 1)
    price = models.IntegerField()
    status = models.CharField(max_length = 50, choices = DELIVERY_STATUS, default = "pending")
    date = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.product.title
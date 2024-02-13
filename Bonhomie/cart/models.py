from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from store.models import Product

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, max_length = 255, on_delete=models.RESTRICT)
    quantity = models.IntegerField(default=1)
    date_added = models.DateTimeField(default = timezone.now)
    
    #returns the string representation of the cart item.
    def __str__(self):
        return (f"{self.quantity} x {self.product}")
    #returns the url of the cart detail page.
    def get_absolute_url(self):
        return reverse("cart")
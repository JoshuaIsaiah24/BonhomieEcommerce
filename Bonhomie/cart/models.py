from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.CharField(max_length = 255)
    quantity = models.IntegerField(default=1)
    #returns the string representation of the cart item.
    def __str__(self):
        return (f"{self.quantity} x {self.product}")
    #returns the url of the cart detail page.
    def get_absolute_url(self):
        return reverse("cart")
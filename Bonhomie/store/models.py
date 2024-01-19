from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length = 255)
    
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length = 255)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    tags = models.ForeignKey(Tag, on_delete = models.RESTRICT)
    brand = models.ForeignKey(Brand, on_delete= models.RESTRICT)
    image = models.ImageField(upload_to= 'uploads/product/', null=True, blank=True)
    
    def __str__(self):
        return self.name
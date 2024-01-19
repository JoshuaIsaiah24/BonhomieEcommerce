from django.contrib import admin
from .models import Tag, Brand, Product

# Register your models here.

admin.site.register(Tag)
admin.site.register(Brand)
admin.site.register(Product)
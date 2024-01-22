from django.contrib import admin
from .models import Tag, Brand, Product, Category

# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Brand)
admin.site.register(Product)
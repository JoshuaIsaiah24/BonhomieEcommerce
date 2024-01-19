from django.shortcuts import render
from .models import Tag, Brand, Product

# Create your views here.

def home(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def shop(request):
    products = Product.objects.all()
    tags = Tag.objects.all()
    brands = Brand.objects.all()
    
    # Filtering by tag
    tag_filter = request.GET.get('tag')
    if tag_filter:
        products = products.filter(tags__name=tag_filter)

    # Filtering by brand
    brand_filter = request.GET.get('brand')
    if brand_filter:
        products = products.filter(brand__name=brand_filter)

    # Sorting by price
    sort_option = request.GET.get('sort')
    if sort_option == 'low_to_high':
        products = products.order_by('price')
    elif sort_option == 'high_to_low':
        products = products.order_by('-price')
        
    return render(request, 'shop.html', {'products': products, 'tags': tags, 'brands': brands})
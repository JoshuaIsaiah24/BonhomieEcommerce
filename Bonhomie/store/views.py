from django.shortcuts import render, get_object_or_404
from .models import Category, Tag, Brand, Product

# Create your views here.

def home(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def shop(request, category_slug=None):
    # Get all products, categories, tags, and brands initially
    products = Product.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    brands = Brand.objects.all()

    # Filtering by Category
    if category_slug and category_slug != 'all':
        products = products.filter(category__slug=category_slug)

    # Create the initial context dictionary
    context = {
        'categories': categories,
        'products': products,
        'selected_category': category_slug,
        'tags': tags,
        'brands': brands,
    }

    # Filtering by Tag
    tag_filter = request.GET.get('tags')
    if tag_filter:
        products = products.filter(tags__name=tag_filter)

    # Filtering by Brand
    brand_filter = request.GET.get('brand')
    if brand_filter:
        products = products.filter(brand__name=brand_filter)

    # Sorting by Price
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    # Filter products based on the price range
    if min_price and max_price:
        products = products.filter(price__gte=min_price, price__lte=max_price)

    # Update the context dictionary with the filtered products
    context['products'] = products

    return render(request, 'shop.html', context)
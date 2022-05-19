from django.shortcuts import render
from.models import Product

def view_products(request):
    """View to render the products page"""

    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/products.html', context)

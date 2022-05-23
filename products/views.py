from django.shortcuts import render, get_object_or_404
from.models import Product

def view_products(request):
    """View to render the products page"""

    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/products.html', context)


def single_product(request, product_id):
    """View to render an indvidual product page"""

    products = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)    

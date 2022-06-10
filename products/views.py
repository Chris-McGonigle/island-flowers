from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm
from newsletter.forms import SubscriberForm


def view_products(request):
    """View to render the products page"""

    products = Product.objects.all()
    sub_form = SubscriberForm()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))

            if sortkey == "category":
                sortkey = "category__name"

            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(
                    request,
                    "You didn't enter any details. Please check and try again",
                )
                return redirect(reverse("products"))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query
            )
            products = products.filter(queries)

    current_sorting = f"{sort}_{direction}"

    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
        "current_sorting": current_sorting,
        "sub_form": sub_form,
    }
    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """View to render an indvidual product page"""

    product = get_object_or_404(Product, pk=product_id)
    sub_form = SubscriberForm()

    context = {
        "product": product,
        "sub_form": sub_form,
    }

    return render(request, "products/product_detail.html", context)


@login_required
def add_product(request):
    """View to add a product to the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, site owners only!")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, "Successfully added product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request,
                "Failed to add product. Please \
                           check and try again.",
            )
    else:
        form = ProductForm()

    sub_form = SubscriberForm()

    template = "products/add_product.html"
    context = {
        "form": form,
        "sub_form": sub_form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """Method to edit an exisiting store product"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, site owners only!")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request,
                "Failed to update product. Please \
                           check and try again.",
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f"You are editing {product.name}")

    sub_form = SubscriberForm()

    template = "products/edit_product.html"
    context = {
        "form": form,
        "product": product,
        "sub_form": sub_form,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """Method to delete an existing store product"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, site owners only!")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, "Successfully deleted product!")
    return redirect(reverse("products"))

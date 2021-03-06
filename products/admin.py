from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "price",
        "image",
    )

    ordering = ("price",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("friendly_name",)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

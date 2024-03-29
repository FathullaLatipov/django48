from django.contrib import admin

from products.models import CategoryModel, ProductModel, CartModel


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'created_at']
    ordering = ['pk']
    search_fields = ['category_name', 'pk']
    list_filter = ['created_at']


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_title', 'product_price', 'product_created_at']
    ordering = ['pk']
    search_fields = ['product_title']
    list_filter = ['product_created_at']

@admin.register(CartModel)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'user_add_date']
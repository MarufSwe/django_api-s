from django.contrib import admin
from .models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name', 'description', 'image']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'price', 'quantity', 'in_stock', 'supplier_name', 'category']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'order_date', 'shipping_date', 'shipping_address']


class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'price', 'quantity', 'discount', 'order', 'product']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetails, OrderDetailsAdmin)
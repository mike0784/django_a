from django.contrib import admin
from .models import Order, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'create_at']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['total_price', 'date_ordered']

admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)

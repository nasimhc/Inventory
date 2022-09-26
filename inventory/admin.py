from django.contrib import admin
from .models import Product, Brand

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'brand', 'shade' ,'price', 'quantity', 'inventory_value']
    list_editable = ['price', 'quantity']
    search_fields = ['name', 'shade',]

    def inventory_value(self, product):
        return product.quantity * product.price

# admin.site.register(Product, ProductAdmin)
admin.site.register(Brand)

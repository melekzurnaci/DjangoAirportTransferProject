from django.contrib import admin

# Register your models here.
from product.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display =['title', 'status']
    list_filter = ['status']


class ProductAdmin(admin.ModelAdmin):
    list_display =['title', 'category', 'price', 'amount', 'status']
    list_filter = ['status', 'category']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
from django.contrib import admin
from .models import Category, Products, AdditionalFree, BagProduct


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'value')
    search_fields = ('name',)

admin.site.register(Category)
admin.site.register(AdditionalFree)
admin.site.register(BagProduct)

from django.contrib import admin

from .models import Brand, Product


# Register your models here.

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'origin',)
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'kind',)


admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)

from django.contrib import admin
from .models import Product, Images, color, size, Sliders, banner

admin.site.register(Images)
admin.site.register(color)
admin.site.register(size)
admin.site.register(Sliders)
admin.site.register(banner)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name', 'price', 'count', 'brand', 'created_date')
    list_filter = ("brand",)
    search_fields = ('name', 'description', 'brand', 'material')



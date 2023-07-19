from django.contrib import admin
from .models import Product, Images, Color, Size, Sliders, Banner, Category

admin.site.register(Images)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Sliders)
admin.site.register(Banner)
admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "count", "brand")
    list_filter = ("brand",)
    search_fields = ("name", "description", "brand", "material")

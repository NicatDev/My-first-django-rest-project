from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Subcategory)
class ProductImageInline(admin.StackedInline):
    model = ProductImage
    max_num = 10
    extra = 1
admin.site.register(Brand)
admin.site.register(Basket)
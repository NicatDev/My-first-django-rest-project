from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)

class ProductImageInline(admin.StackedInline):
    model = ProductImage
    max_num = 10
    extra = 1

admin.site.register(Basket)
admin.site.register(ProductImage)
from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Type)
admin.site.register(Category)
admin.site.register(Tour)
admin.site.register(TourImage)
admin.site.register(Favourite)
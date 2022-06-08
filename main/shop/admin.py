from django.contrib import admin
from .models import *
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
class offerAdmin(admin.ModelAdmin):
    list_display = ('stock', 'discription')

admin.site.register(Product)
admin.site.register(offer)

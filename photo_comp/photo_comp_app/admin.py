from django.contrib import admin
from photo_comp_main.models import Products, Categories, Image

# Register your models here.
admin.site.register(Categories)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    fields = ('title', 'image')


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    fields = ('name', ('price', 'category'), 'image')
    search_fields = ('name',)
    ordering = ('name', 'price', 'category')

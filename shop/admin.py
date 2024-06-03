from django.contrib import admin
from .models import Category,Product,Contact


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name","slug_field","created_at","updated_at")
    search_fields = ("category_name",)
    prepopulated_fields = {"slug_field":("category_name",)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name","category","price","created_at","updated_at")
    search_fields = ("product_name","category__category_name")
    list_filter = ("category",)
    prepopulated_fields = {"slug_field": ("product_name",)}

class ContactAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","email","feedback")
    search_fields = ("first_name","last_name")
    list_filter = ("first_name","last_name")

# Register your models here.

admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Contact,ContactAdmin)

from django.contrib import admin
from .models import Category, Product
# Register your models here.



class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']
    # list_editable=['image','desc']
    prepopulated_fields={'slug':('name',)}
    
admin.site.register(Category,CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug': ('name',)}
    list_display=['name','price','category', 'stock', 'available', 'created', 'updated', 'image']
    list_editable=['price','stock','available','image']
    list_per_page=20


admin.site.register(Product,ProductAdmin)

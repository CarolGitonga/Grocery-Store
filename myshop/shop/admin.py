from django.contrib import admin
from .models import Cart, Cartitems, Category, Product

# Register your models here.
@admin.register(Category)
class CatergoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('name',)}#to specify fields where the value is automatically set using the value of other fields

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','available','created','updated']
    list_filter = ['available','created','updated']
    list_editable = ['price','available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Cart)
admin.site.register(Cartitems)

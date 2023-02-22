from django.contrib import admin
from .models import Product, Category,CategoryParent
from reviews.models import review
# Register your models here.
class reviewInline(admin.TabularInline):
    model = review
class productAdmin(admin.ModelAdmin):
    inlines = (reviewInline,)
    readonly_fields = ('id',)
    list_display =('id','title')


class categoryInline(admin.TabularInline):
    model = Category    
class parentCategoryAdmin(admin.ModelAdmin):
    inlines=(categoryInline,)

class categoryProductInline(admin.TabularInline):
    model = Product
class categoryAdmin(admin.ModelAdmin):
    inlines = (categoryProductInline,)

admin.site.register(Product, productAdmin)
admin.site.register(Category, categoryAdmin)
admin.site.register(CategoryParent, parentCategoryAdmin)
from django.contrib import admin
from .models import Product, Category,CategoryParent
from reviews.models import review
# Register your models here.
class reviewInline(admin.TabularInline):
    model = review
class productAdmin(admin.ModelAdmin):
    inlines = (reviewInline,)
admin.site.register(Product, productAdmin)
admin.site.register(Category)
admin.site.register(CategoryParent)
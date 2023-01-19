from django.contrib import admin
from .models import review

# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display=('product',)    
admin.site.register(review, ReviewAdmin)

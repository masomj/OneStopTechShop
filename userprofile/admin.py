from django.contrib import admin
from .models import userDetails

# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display=(
        'user_id',
    )

admin.site.register(userDetails, userAdmin)


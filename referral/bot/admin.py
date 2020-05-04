from django.contrib import admin

from .models import User
# Register your models here.
@admin.site.register(User)
class UserProfile(admin.ModelAdmin):
    list_display = ('id', 'name', 'username')
    

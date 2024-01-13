from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'profile_image']  # Agregar más campos si es necesario

admin.site.register(CustomUser, CustomUserAdmin)

from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = UserAdmin
    add_form = CustomUserForm
    
    fieldsets = UserAdmin.fieldsets + (
        'Role', 
        {
            'fields': ('is_admin', 'is_alumni')
        }
    )

admin.site.register(CustomUser)
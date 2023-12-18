# C:\ApplicationProjects\Lindy_Assesser\user_management\admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm 

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'full_name', 'is_staff', 'is_active']
    list_filter = ['email', 'full_name', 'is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('email', 'full_name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ['email', 'full_name']
    # Default ordering was based on 'username' but our model uses 'email'
    ordering = ['email']

admin.site.register(CustomUser, CustomUserAdmin)
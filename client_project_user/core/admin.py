from django.contrib import admin
from .models import Client, Project
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff')



admin.site.register(Client)
admin.site.register(Project)

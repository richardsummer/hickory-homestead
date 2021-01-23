from django.contrib import admin
from django.contrib.contrib.auth.admin import UserAdmin
from .models import User, Profile

admin.site.register(User, UserAdmin)
admin.site.register(Profile)

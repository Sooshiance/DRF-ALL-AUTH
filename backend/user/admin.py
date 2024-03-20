from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from .models import User, Profile, UserOTP


class Admin(UserAdmin):
    list_display = ['phone', 'username', 'email', 'is_active']
    filter_horizontal = []
    list_filter = []
    fieldsets = []
    search_fields = ['phone', 'username']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone']
    search_fields = ['phone']


class OTPAdmin(admin.ModelAdmin):
    list_display = ['user', 'otp']


admin.site.register(User, Admin)

admin.site.register(Profile, ProfileAdmin)

admin.site.register(UserOTP, OTPAdmin)

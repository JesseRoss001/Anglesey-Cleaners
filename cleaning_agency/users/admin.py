from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, CustomerProfile, GeneralLocation
admin.site.register(GeneralLocation)
# Customize the User admin
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('is_customer', 'is_cleaner', 'is_admin', 'contact_number', 'approved', 'hourly_rate', 'image', 'general_area', 'selected_areas')}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {'fields': ('is_customer', 'is_cleaner', 'is_admin', 'contact_number', 'approved', 'hourly_rate', 'image', 'general_area', 'selected_areas')}),
    )
    list_display = ('username', 'email', 'is_customer', 'is_cleaner', 'is_admin', 'approved')
    search_fields = ('username', 'email')
    filter_horizontal = ('selected_areas',)

# Register your models here
admin.site.register(User, UserAdmin)

class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'postcode', 'city')
    search_fields = ('user__username', 'postcode', 'city')
    filter_horizontal = ('selected_areas',)

admin.site.register(CustomerProfile, CustomerProfileAdmin)
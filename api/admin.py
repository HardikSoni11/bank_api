from django.contrib import admin
from .models import BankDetail

# admin.site.register(BankDetail)

@admin.register(BankDetail)
class BankDetailAdmin(admin.ModelAdmin):
    list_display = ['ifsc', 'bank_id', 'branch', 'address', 'city', 'district', 'state', 'bank_name']
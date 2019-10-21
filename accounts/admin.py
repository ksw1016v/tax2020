from django.contrib import admin
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin

from .models import*

class AccountAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ['time_stamp','user_name','team','phone']

class SalesAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ['time_stamp','name','team','phone','referrer_name','memo']
# Register your models here.

admin.site.register(Account,AccountAdmin)
admin.site.register(Sales,SalesAdmin)


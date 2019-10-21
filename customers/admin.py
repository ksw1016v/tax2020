from django.contrib import admin
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin


from .models import*
class CustomerAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ['time_stamp','company','category','sales','name','phone','location','address','bizsub','memo','sub_company']

# Register your models here.
admin.site.register(Customer,CustomerAdmin)

from django.contrib import admin
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin

from .models import*
class WorkAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ['work_name','Requirements1','Requirements2','Requirements3','support_period','support_amount','memo']


class WorkingAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ['company','work_name','ing','support_amount','created','updated','pay_per','fee_per','memo']


class ResultAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ['work_name','work_date','work_category','work_result','amount','amount_duedate','amount_date','amount_memo','created','updated','pay','pay_date','pay_memo','fee','fee_tax','fee_date','fee_memo']

# Register your models here.
admin.site.register(Work,WorkAdmin)
admin.site.register(Working,WorkingAdmin)
admin.site.register(Result,ResultAdmin)

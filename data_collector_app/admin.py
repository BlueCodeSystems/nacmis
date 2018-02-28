from django.contrib import admin

from .models import ReportDetail

# Register your models here.

class ReportDetailAdmin(admin.ModelAdmin):
    fields = ['report_date', 'quarter', 'name', 'report_type', 'location']

# admin.site.register(ReportDetail)
admin.site.register(ReportDetail, ReportDetailAdmin)
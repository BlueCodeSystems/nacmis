from django.contrib import admin

from .models import ContactDetails

# Register your models here.

class ReportDetailAdmin(admin.ModelAdmin):
    fields = ['report_date', 'quarter', 'name', 'organization_type', 'location']

admin.site.register(ContactDetails)
# admin.site.register(ReportDetail, ReportDetailAdmin)
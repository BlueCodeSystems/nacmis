from django.contrib import admin

from .models import GeographicActivities

# Register your models here.

class ReportDetailAdmin(admin.ModelAdmin):
    fields = ['report_date', 'quarter', 'name', 'organization_type', 'location']

admin.site.register(GeographicActivities)
# admin.site.register(ReportDetail, ReportDetailAdmin)
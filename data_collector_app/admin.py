from django.contrib import admin

from .models import BasicDetail, ContactDetail, GeographicActivity, \
    FundingSource, TargetGroupMessage

# Register your models here.

class ReportDetailAdmin(admin.ModelAdmin):
    fields = ['report_date', 'quarter', 'name', 'organization_type', 'location']

# Register StakeHolder models
admin.site.register(BasicDetail)
admin.site.register(ContactDetail) 
admin.site.register(GeographicActivity)
admin.site.register(FundingSource)
admin.site.register(TargetGroupMessage)
# admin.site.register(ReportDetail, ReportDetailAdmin)

#
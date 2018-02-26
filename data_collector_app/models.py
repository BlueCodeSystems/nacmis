from django.db import models

# Create your models here.

#               REPORT DETAIL FORM
# *************************************************
class ReportDetail(models.Model):
    report_date = models.DateTimeField('date of report')
    quarter = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    report_type = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    reporter_name = models.CharField(max_length=100)
    reporter_phone = models.CharField(max_length=50)
    reporter_email = models.CharField(max_length=100)

# HIV ACTIVITIES ORGANIZATION PARTICIPATES IN FORM
# *************************************************


#               STAKEHOLDER DIRECTORY
# *************************************************

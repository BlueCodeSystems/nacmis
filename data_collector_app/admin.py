from django import forms
from django.contrib import admin

from .models import (ActivityReportForm, StakeHolder, OrganizationTarget, GeographicActivity, FundingSources,
TargetGroupPreventionMessages)

from .models import(IECMaterial, AdolecentsReached, OutOfSchool, SexWorker, Inmate, CorrectionalFaciltyStaff, 
PersonsWithDisabilty, MobileWorker, MenWithMen, CondomProgramming, CriticalEnabler, SynergyDevelopmentSector, 
CommunityHealthSystem, VulnerablePeople)

# INLINES FOR STAKEHOLDER DIRECTORY ADMIN
# *************************************************
class GeographicActivityInline(admin.TabularInline):
    model = GeographicActivity
    extra = 1

class FundingSourcesInline(admin.TabularInline):
    model = FundingSources
    extra = 1

class TargetGroupPreventionMessagesInline(admin.TabularInline):
    model = TargetGroupPreventionMessages
    extra = 1


# INLINES FOR ACTIVITY REPORT FORM ADMIN
# *************************************************
class MaterialInline(admin.TabularInline):
    model = IECMaterial
    extra = 1

class AdolencentsInline(admin.TabularInline):
    model = AdolecentsReached
    extra = 1

class OutOfSchoolInline(admin.TabularInline):
    model = OutOfSchool
    extra = 1

class SexWorkerInline(admin.TabularInline):
    model = SexWorker
    extra = 1

class InmateInline(admin.TabularInline):
    model = Inmate
    extra = 1

class CorrectionalFaciltyStaffInline(admin.TabularInline):
    model = CorrectionalFaciltyStaff
    extra = 1

class PersonsWithDisabiltyInline(admin.TabularInline):
    model = PersonsWithDisabilty
    extra = 1

class MobileWorkerInline(admin.TabularInline):
    model = MobileWorker
    extra = 1

class MenWithMenInline(admin.TabularInline):
    model = MenWithMen
    extra = 1

class CondomProgrammingInline(admin.TabularInline):
    model = CondomProgramming
    extra = 1

class SynergyDevelopmentSectorInline(admin.TabularInline):
    model = SynergyDevelopmentSector
    extra = 1

class CommunityHealthSystemInline(admin.TabularInline):
    model = CommunityHealthSystem
    extra = 1

class VulnerablePeopleInline(admin.TabularInline):
    model = VulnerablePeople
    extra = 1

# ADMIN CLASSES
# *************************************************
class StakeHolderAdmin(admin.ModelAdmin):
    
    fieldsets = (
        (None, {
            'fields': ('organization_name', 'start_year', 'permanent_employee_female', 
            'permanent_employee_male', 'temporary_employee_female', 'temporary_employee_male', 
            'volunteer_employee_female', 'volunteer_employee_male', 'description_of_organization')
        }),
        ('Contact details', {
            'fields': ('key_contact_name', 'position_within_organization', 'organization_district', 
            'organization_address', 'telephone_number', 'telephone_number_alternative', 'email_address', 
            'organization_type', 'organization_target')
        })
    )

    inlines = [GeographicActivityInline, FundingSourcesInline, TargetGroupPreventionMessagesInline]


class ActivityReportFormAdmin(admin.ModelAdmin):
    AdolencentsInline.max_num = 1
    OutOfSchoolInline.max_num = 1
    SexWorkerInline.max_num = 1
    InmateInline.max_num = 1
    CorrectionalFaciltyStaffInline.max_num = 1
    PersonsWithDisabiltyInline.max_num = 1
    MobileWorkerInline.max_num = 1
    MenWithMenInline.max_num = 1
    CondomProgrammingInline.max_num = 1
    SynergyDevelopmentSectorInline.max_num = 1
    CommunityHealthSystemInline.max_num = 1
    VulnerablePeopleInline.max_num = 1

    inlines = [MaterialInline, AdolencentsInline, OutOfSchoolInline, SexWorkerInline, InmateInline, 
        CorrectionalFaciltyStaffInline, PersonsWithDisabiltyInline, MobileWorkerInline, MenWithMenInline,
        CondomProgrammingInline, SynergyDevelopmentSectorInline, CommunityHealthSystemInline, 
        VulnerablePeopleInline]

class OrganizationTargetAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Organization Target', {
            'fields': ('organization_target_option',)
        }),
    )


# Register StakeHolder models
admin.site.register(StakeHolder, StakeHolderAdmin)

# Register HIV Activities Organization Participates in
admin.site.register(ActivityReportForm, ActivityReportFormAdmin)

# note: uncomment to have a user be flexible to enter there own targets to the list
# admin.site.register(OrganizationTarget, OrganizationTargetAdmin)

# admin.site.register(GeographicActivity)

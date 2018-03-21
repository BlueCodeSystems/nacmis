from django import forms
from django.contrib import admin

from .models import (ActivityReportForm, StakeHolder, OrganizationTarget, GeographicActivity, FundingSources,
TargetGroupPreventionMessages)
from .models import(IECMaterial, AdolecentsReached, OutOfSchool, SexWorker, Inmate, CorrectionalFaciltyStaff, 
PersonsWithDisabilty, MobileWorker, MenWithMen, CondomProgramming, CriticalEnabler, SynergyDevelopmentSector, 
CommunityHealthSystems, VulnerablePeople)

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
    extra = 3

class AdolencentsInline(admin.TabularInline):
    model = AdolecentsReached
    extra = 3

class OutOfSchoolInline(admin.TabularInline):
    model = OutOfSchool
    extra = 3

class SexWorkerInline(admin.TabularInline):
    model = SexWorker
    extra = 3

class InmateInline(admin.TabularInline):
    model = Inmate
    extra = 3

class CorrectionalFaciltyStaffInline(admin.TabularInline):
    model = CorrectionalFaciltyStaff
    extra = 3

class PersonsWithDisabiltyInline(admin.TabularInline):
    model = PersonsWithDisabilty
    extra = 3

class MobileWorkerInline(admin.TabularInline):
    model = MobileWorker
    extra = 3

class MenWithMenInline(admin.TabularInline):
    model = MenWithMen
    extra = 1

class CondomProgrammingInline(admin.TabularInline):
    model = CondomProgramming
    extra = 1

class SynergyDevelopmentSectorInline(admin.TabularInline):
    model = SynergyDevelopmentSector
    extra = 3

class CommunityHealthSystemsInline(admin.TabularInline):
    model = CommunityHealthSystems
    extra = 3

class VulnerablePeopleInline(admin.TabularInline):
    model = VulnerablePeople
    extra = 3

# ADMIN CLASSES
# *************************************************
'''
 ('Geographic activities - High impact interventions', {
            'fields':('elimination_of_mother_child_transmission', 'condom_programming', 
            'voluntary_medical_male_circumcision', 'hiv_counselling_testing', 
            'social_behaviour_change', 'anti_retroviral_treatment')
        }),
        ('Geographic activities - Critical enablers', {
            'fields':('gender_equality_empowerment', 'laws_legal_policies_practices', 
            'leadership_commitment_good_governance', 'resource_mobilization_sustainable_financing' )
        }),
        ('Geographic activities - Synergies with development sectors', {
            'fields':('post_exposure_prophylaxis', 'blood_safety', 'poverty_alleviation_livelihoods',
            'food_nutrition_security', 'mainstreaming_hiv_into_capital_projects')
        }),
'''
class StakeHolderAdmin(admin.ModelAdmin):

    inlines = [GeographicActivityInline, FundingSourcesInline, TargetGroupPreventionMessagesInline]


class ActivityReportFormAdmin(admin.ModelAdmin):
    
    inlines = [MaterialInline, AdolencentsInline, OutOfSchoolInline, SexWorkerInline, InmateInline, 
        CorrectionalFaciltyStaffInline, PersonsWithDisabiltyInline, MobileWorkerInline, MenWithMenInline,
        CondomProgrammingInline, SynergyDevelopmentSectorInline, CommunityHealthSystemsInline, 
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

admin.site.register(OrganizationTarget, OrganizationTargetAdmin)
admin.site.register(GeographicActivity)

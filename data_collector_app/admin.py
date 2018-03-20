from django import forms
from django.contrib import admin

from .models import (StakeHolder, OrganizationTarget, GeographicActivity, FundingSources,
TargetGroupPreventionMessages)

from .models import (MaterialInline, AdolencentsInline, OutOfSchoolInline, SexWorkerInline, InmateInline, 
        CorrectionalFaciltyStaffInline, PersonsWithDisabiltyInline, MobileWorkerInline, MenWithMenInline,
        CondomProgrammingInline, SynergyDevelopmentSectorInline, CommunityHealthSystemsInline, 
        VulnerablePeopleInline)

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
    fieldsets = (
        ('Types of care and support organization provides', {
            'fields':('food_and_nutrition', 'shelter_and_care', 'protection_and_legal_aid', 'healthcare', 
                'psychosocial', 'social_support', 'spiritual_support', 'education_and_vocational_training', 
                'economic_strengthening')
        }),
        ('Monitoring and Evaluation', {
            'fields':('nacmis', 'hmis', 'datim', 'internal_system', 'systems_other')
        })
        
    )

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
#admin.site.register(ActivityReportForm, ActivityReportFormAdmin)

admin.site.register(OrganizationTarget, OrganizationTargetAdmin)
admin.site.register(GeographicActivity)

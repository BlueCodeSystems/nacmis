from django import forms
from django.contrib import admin

from .models import (StakeHolderDirectory, IECMaterial, AdolecentsReached, ActivityReportForm,
OutOfSchool, SexWorker, Inmate, CorrectionalFaciltyStaff, PersonsWithDisabilty, MobileWorker, 
MenWithMen, CondomProgramming, SynergyDevelopmentSector, CommunityHealthSystems, 
VulnerablePeople, OrganizationTarget)

# INLINES FOR STAKEHOLDER DIRECTORY ADMIN
# *************************************************

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

class OrganizationTargetInline(admin.StackedInline):
    # Wont' work... this is for one to one relationship
    model = OrganizationTarget
    extra = 1

# ADMIN CLASSES
# *************************************************
class StakeHolderDirectoryAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Basic details on the organization', {
            'fields': ('organization_name', 'start_year', ('permanent_employee_female', 
            'permanent_employee_male', 'temporary_employee_female', 'temporary_employee_male', 
            'volunteer_employee_female', 'volunteer_employee_male'), 'description')
        }),
        ('Contact details', {
            'fields': ('contact_name', 'contact_organization', 'contact_address', 
            'phone', 'alternative_phone', 'email', 'website' )
        }),
        ('Organization classification', {
            'fields':( 'organization_type', 'organization_target_form' )
        }),
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
        ('Funding sources', {
            'fields':('funder_organization', 'funder_support_type', 'amount', 'comment')
        }),
        ('Target groups and prevention messages', {
            'fields':('condom_use', 'mc_information', 'mcp_information', 'pmtct_promotion', 
            'vct_hct_promotion', 'pep_information', 'sti_information', 'tb_information', 
            'gbv_information', 'social_norms', 'message_other')
        })
    )

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
            'fields': ('plhiv', 'ovc', 'pregnant_women', 'care_givers', 'health_workers', 'teachers', 
                'children', 'adolecents', 'old_people', 'disabled_people', 'inmates_wivies', 
                'govt_workers', 'sex_workers', 'church_leaders', 'employee_families','gdwg', 
                'idu', 'msm', 'mobile_population', 'out_of_school_youth', 'inmates', 
                'street_children', 'traditional_healers', 'traditional_leaders', 'target_others')
        }),
    )

'''
class IECMaterialAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Social behaviour change communication', {
            'fields':('material_type', 'number_distributed', 'iec_localized')
        })
    )

class AdolecentsReachedAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Social behaviour change communication for key populations', {
            'fields':('adolescents_female_10_14', 'adolescents_female_15_19', 'adolescents_female_20_24', 
                'adolescents_male_10_14', 'adolescents_male_15_19', 'adolescents_male_20_24')
        } )
    )

class OutOfSchoolAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields':('out_school_female_10_14', 'out_school_female_15_19', 'out_school_female_20_24', 
                'out_school_male_10_14', 'out_school_male_15_19', 'out_school_male_20_24')
        } )
    )

class SexWorkerAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields':('sex_workers_female_num', 'sex_workers_male_num')
        })
    )

class InmateAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields':('inmates_female_num', 'inmates_male_num')
        })
    )

class CorrectionalFaciltyStaffAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields':('correctional_staff_female_num', 'correctional_staff_male_num')
        })
    )

class PersonsWithDisabiltyAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields':( 'pwd_female_num', 'pwd_male_num')
        })
    )

class MobileWorkerAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields':('mobile_workers_female_num', 'mobile_workers_male_num')
        })
    )

class MenWithMenAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields':('men_with_men')
        })
    )

class CondomProgrammingAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Condom programming', {
            'fields':('condom_dist_point_num', 'female_condom_distributed_num', 'male_condom_distributed_num')
        })
    )

class CriticalEnablerAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Crtical enablers', {
            'fields':('accessed_pep_female_num', 'accessed_pep_male_num')
        })
    )
class SynergyDevelopmentSectorAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Synergies with other development sectors', {
            'fields':('employees_reached_female_num', 'employees_reached_male_num')
        })
    )

class CommunityHealthSystemsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Community health systems', {
            'fields':('plhiv_female_num', 'plhiv_male_num', 'ovc_female_num', 'ovc_male_num')
        })
    )
# also under community systems
class VulnerablePeopleAdmin(admin.ModelAdmin):
    fieldsets = (
        ('', {
            'fields':('ovc_care_support_0_9', 'ovc_care_support_10_14', 'ovc_care_support_15_19', 
            'ovc_care_support_20_24', 'ovc_care_support_25_plus')
        })
    )
'''
myList = [StakeHolderDirectory, OrganizationTarget]
# Register StakeHolder models
admin.site.register(StakeHolderDirectory, StakeHolderDirectoryAdmin)

# Register HIV Activities Organization Participates in
admin.site.register(ActivityReportForm, ActivityReportFormAdmin)

admin.site.register(OrganizationTarget, OrganizationTargetAdmin)
from django import forms
from django.contrib import admin

from .models import StakeHolderDirectory, IECMaterial, NameMeCorrectlyAfterTheQuestion, ActivityReportForm

# Register your models here.
class MaterialInline(admin.StackedInline):
    model = IECMaterial
    extra = 3

class StakeHolderDirectoryAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Basic details on the organization', {
            'fields': ('organization_name', 'start_year', 'permanent_employee_female', 
            'permanent_employee_male', 'temporary_employee_female', 'temporary_employee_male', 
            'volunteer_employee_female', 'volunteer_employee_male', 'description')
        }),
        ('Contact details', {
            'fields': ('contact_name', 'contact_organization', 'contact_address', 
            'phone', 'alternative_phone', 'email', 'website' )
        }),
        ('Organization classification', {
            'fields':('organization_type', 'plhiv', 'ovc', 'pregnant_women', 
            'care_givers', 'health_workers', 'teachers', 'children', 'adolecents', 
            'old_people', 'disabled_people', 'inmates_wivies', 'govt_workers', 
            'sex_workers', 'church_leaders', 'employee_families', 'gdwg', 
            'idu', 'msm', 'mobile_population', 'out_of_school_youth', 'inmates', 
            'street_children', 'traditional_healers', 'traditional_leaders', 
            'target_others' )
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
        ('Condom programming', {
            'fields':('condom_dist_point_num', 'female_condom_distributed_num', 'male_condom_distributed_num')
        }),
        ('Crtical enablers', {
            'fields':('accessed_pep_female_num', 'accessed_pep_male_num')
        }),
        ('Synergies with other development sectors', {
            'fields':('employees_reached_female_num', 'employees_reached_male_num')
        }),
        ('Community health systems', {
            'fields':('plhiv_female_num', 'plhiv_male_num', 'ovc_female_num', 'ovc_male_num', 
            'ovc_care_support_0_9', 'ovc_care_support_10_14', 'ovc_care_support_15_19', 'ovc_care_support_20_24', 
            'ovc_care_support_25_plus')
        }),
        ('Types of care and support organization provides', {
            'fields':('food_and_nutrition', 'shelter_and_care', 'protection_and_legal_aid', 'healthcare', 
                'psychosocial', 'social_support', 'spiritual_support', 'education_and_vocational_training', 
                'economic_strengthening')
        }),
        ('Monitoring and Evaluation', {
            'fields':('nacmis', 'hmis', 'datim', 'internal_system', 'systems_other')
        })
        
    )

class NameMeCorrectlyAfterTheQuestionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Social behaviour change communication for key populations', {
            'fields':('adolescents_female_10_14', 'adolescents_female_15_19', 'adolescents_female_20_24', 
                'adolescents_male_10_14', 'adolescents_male_15_19', 'adolescents_male_20_24',
                'out_school_female_10_14', 'out_school_female_15_19', 'out_school_female_20_24', 
                'out_school_male_10_14', 'out_school_male_15_19', 'out_school_male_20_24',
                'sex_workers_female_num', 'sex_workers_male_num', 'inmates_female_num', 'inmates_male_num', 
                'correctional_staff_female_num', 'correctional_staff_male_num', 'pwd_female_num', 
                'pwd_male_num', 'mobile_workers_female_num', 'mobile_workers_male_num', 'men_with_men')
        } )
    )

class IECMaterialAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Social behaviour change communication', {
            'fields':('material_type', 'number_distributed', 'iec_localized')
        }),
    )

    inlines = [MaterialInline]

# using iteratable to store multiple models
# model_list = [IECMaterial, NameMeCorrectlyAfterTheQuestion, ActivityReportForm]

# Register StakeHolder models
admin.site.register(StakeHolderDirectory, StakeHolderDirectoryAdmin)

# Register HIV Activities Organization Participates in
admin.site.register(ActivityReportForm, ActivityReportFormAdmin)

# ERROR: 
# admin.site.register(IECMaterial, IECMaterialAdmin)
admin.site.register(IECMaterial)
# admin.site.register()
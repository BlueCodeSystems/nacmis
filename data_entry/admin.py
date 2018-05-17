from django import forms
from django.contrib import admin

from .models import NationalOrganisation, ActivityReportForm, StakeholderDirectory, \
OrganisationTarget, MobilePopulation, SupportField, ProgramActivity, FundingSource, TargetGroupPreventionMessage, \
OtherQuestion, EndOfYearQuestion, GeneralComment

from .models import IECMaterial, Teachers, OutOfSchool, SexWorker, Inmate, PersonsWithDisabilty, MobileWorker, \
MenWithMen, TransgenderIndividual, PeopleWhoInjectDrug, CondomProgramming, CriticalEnabler, \
SynergyDevelopmentSector, CommunityHealthSystem, VulnerablePeople

from .forms import StakeholderDirectoryModelForm, ProgramActivityModelForm, TargetGroupPreventionMessageModelForm

# INLINES FOR STAKEHOLDER DIRECTORY ADMIN
# *************************************************
class ProgramActivityInline(admin.TabularInline):
    model = ProgramActivity
    verbose_name_plural = 'Program activities'
    form = ProgramActivityModelForm
    extra = 1

class FundingSourceInline(admin.TabularInline):
    model = FundingSource
    extra = 1

class TargetGroupPreventionMessageInline(admin.TabularInline):
    model = TargetGroupPreventionMessage
    form = TargetGroupPreventionMessageModelForm
    extra = 1

class OtherQuestionInline(admin.TabularInline):
    model = OtherQuestion
    extra = 1

class EndOfYearQuestionInline(admin.TabularInline):
    model = EndOfYearQuestion
    extra = 1

class GeneralCommentInline(admin.StackedInline):
    model = GeneralComment
    extra = 1

# INLINES FOR ACTIVITY REPORT FORM ADMIN
# *************************************************
class MaterialInline(admin.TabularInline):
    model = IECMaterial
    verbose_name = 'IEC Material'
    verbose_name_plural = 'How many Information Education Communication(IEC) materials were distributed by \
        your organisation this quarter? Which of your materials were localized? (produced according to \
        local condition, culture, language etc.)'
    extra = 1

class TeachersInline(admin.TabularInline):
    model = Teachers
    verbose_name_plural = 'Number of teachers who have received training, and taught lessons, in life \
        skills based comprehensive sexuality eduaction this quarter'
    extra = 1

class OutOfSchoolInline(admin.TabularInline):
    model = OutOfSchool
    verbose_name_plural = 'Number of Out of School children and young people aged 10-24 years provided \
        with life skills- based comprehensive sexuality education within this quarter'
    extra = 1

class SexWorkerInline(admin.TabularInline):
    model = SexWorker
    verbose_name_plural = 'How many sex workers were reached with HIV prevention programmes by your \
        organisation this quarter?'
    extra = 1

class InmateInline(admin.TabularInline):
    model = Inmate
    verbose_name_plural = 'How many inmates were reached with HIV prevention programmes by your organisation \
        this quarter?'
    extra = 1

class PersonsWithDisabiltyInline(admin.TabularInline):
    model = PersonsWithDisabilty
    verbose_name_plural = 'How many persons with disability were reached with HIV prevention programmes by your \
        organisation this quarter?'
    extra = 1

class MobileWorkerInline(admin.TabularInline):
    model = MobileWorker
    verbose_name_plural = 'How many mobile workers were reached with HIV prevention programmes by your organisation \
        this quarter?'
    extra = 1

class MenWithMenInline(admin.TabularInline):
    model = MenWithMen
    verbose_name_plural = 'How many men who have sex with men (MSM) were reached with HIV prevention programmes by \
        your organisation this quarter?'
    extra = 1

class TransgenderIndividualInline(admin.TabularInline):
    model = TransgenderIndividual
    verbose_name_plural = 'How many transgender individuals were reached with HIV prevention programmes by your \
        organisation this quarter?'
    extra = 1

class PeopleWhoInjectDrugInline(admin.TabularInline):
    model = PeopleWhoInjectDrug
    verbose_name_plural = 'Number of adolescents and young people aged 10-24 reached by IEC materials \
        by your organisation this quarter'
    extra = 1

class CondomProgrammingInline(admin.TabularInline):
    model = CondomProgramming
    verbose_name_plural = 'How many condom service distribution points were supplied by your organisation this \
        quarter? (*excluding health facilities) How many male and/or female condoms were distributed to end users by \
        your organisation this quarter (*excluding health facilities)?'
    extra = 1

class CriticalEnablerInline(admin.TabularInline):
    model = CriticalEnabler
    verbose_name_plural = 'Number of people who experienced physical or sexual violence and were referred for Post \
        Exposure Prophylaxis (PEP) within 72 hours in accordance with national guidelines this quarter.'
    extra = 1
    
class SynergyDevelopmentSectorInline(admin.TabularInline):
    model = SynergyDevelopmentSector
    verbose_name_plural = 'How many employees were reached through workplace programmes by your organisation this quarter?'
    extra = 1

class CommunityHealthSystemInline(admin.TabularInline):
    model = CommunityHealthSystem
    verbose_name_plural = 'How many PLHIV support groups set up by your organisation are currently active? How many PLHIV \
        are currently enrolled in the active PLHIV support groups by your organisation?'
    extra = 1

class VulnerablePeopleInline(admin.TabularInline):
    model = VulnerablePeople
    verbose_name_plural = 'How many vulnerable people in total received care and support from your organisation this \
    quarter? What types of care and support does your organisation provide? (select all that apply)'
    extra = 1

# ADMIN CLASSES
# *************************************************
class StakeholderDirectoryAdmin(admin.ModelAdmin):
    list_filter = ('national_organisation', 'organisation_district')
    list_display = ('organisation', 'key_contact_name', 'telephone_number', 'start_year')

    form = StakeholderDirectoryModelForm

    MenWithMenInline.max_num = 1
    TeachersInline.max_num = 1
    CondomProgrammingInline.max_num = 1
    CriticalEnablerInline.max_num = 1
    SynergyDevelopmentSectorInline.max_num = 1
    CommunityHealthSystemInline.max_num = 1
    MenWithMenInline.max_num = 1
    CondomProgrammingInline.max_num = 1
    CriticalEnablerInline.max_num = 1
    SynergyDevelopmentSectorInline.max_num = 1
    CommunityHealthSystemInline.max_num = 1
    OtherQuestionInline.max_num = 1
    EndOfYearQuestionInline.max_num = 1
    GeneralCommentInline.max_num = 1
    
    fieldsets = (
        ('Basic details on the organisation', {
            #'classes':('collapse',),
            'fields': ('national_organisation','organisation', 'organisation_district','organisation_address', 
            'start_year', 'gps', 'website', 'description_of_organisation')
        }),
        ('Contact details', {
            'fields': ('key_contact_name', 'position_within_organisation', 'telephone_number', 
            'telephone_number_alternative', 'email_address'),
        }),
        ('Staff details', {
            'fields': ( ('permanent_employee_female', 'permanent_employee_male'), ('temporary_employee_female', 
                'temporary_employee_male'), ('volunteer_employee_female', 'volunteer_employee_male') ),
            'description':('<b><p class="description_fit_in">Employee\'s fall in different groups. Permanent employees \
                are those who is hired to work without any time frame for his/her exit. Temporary employees are those that \
                are hired for a limited period of time. <br/>They are usually hired on a casual, part-time, or full-time \
                basis, but the employment is temporary. Volunteer employees donate their time and energy without receiving \
                financial gain. These employees <br/>usually do not displace any other employee types and usually not \
                entitled to many benefits as compared to other employee types.</p></b>'),
        }),
        ('organisation classification', {
            'fields': ('organisation_type', 'organisation_target')
        })
    )

    inlines = [ProgramActivityInline, FundingSourceInline, TargetGroupPreventionMessageInline,
        OtherQuestionInline, EndOfYearQuestionInline, GeneralCommentInline]

    class Media:
        css = { "all" : ("css/hide_admin_original.css",) }

class ActivityReportFormAdmin(admin.ModelAdmin):
    list_filter = ('location_province', 'location_district',)
    list_display = ('stake_holder_name', 'location_district', 'quarter_been_reported')
    
    PeopleWhoInjectDrugInline.max_num = 1
    OutOfSchoolInline.max_num = 1
    SexWorkerInline.max_num = 1
    InmateInline.max_num = 1
    TransgenderIndividualInline.max_num = 1
    PersonsWithDisabiltyInline.max_num = 1
    MobileWorkerInline.max_num = 1
    MenWithMenInline.max_num = 1
    CondomProgrammingInline.max_num = 1
    CriticalEnablerInline.max_num = 1
    SynergyDevelopmentSectorInline.max_num = 1
    CommunityHealthSystemInline.max_num = 1
    VulnerablePeopleInline.max_num = 1

    fieldsets = (
        ('Contact details', {
            'fields':('report_date', 'quarter_been_reported', 'stake_holder_name', 
            ('location_province', 'location_district', ), ('name', 
            'telephone_number', 'email_address')
            ),
        }),
        ('What types of care and support does your organisation provide? (select all that apply)', {
            'fields': ('food_and_nutrition', 'shelter_and_care', 'protection_and_legal_aid', 'healthcare', 
            'psychosocial', 'social_support', 'spiritual_support', 'education_and_vocational_training',
            'economic_strengthening'),
        }),
    )

    inlines = [MaterialInline, TeachersInline, OutOfSchoolInline, SexWorkerInline, InmateInline, PersonsWithDisabiltyInline, 
        MobileWorkerInline, MenWithMenInline, TransgenderIndividualInline, PeopleWhoInjectDrugInline,CondomProgrammingInline, 
        CriticalEnablerInline, SynergyDevelopmentSectorInline, CommunityHealthSystemInline, VulnerablePeopleInline]

    class Media:
        css = { "all" : ("css/hide_admin_original.css",) }

class OrganisationTargetAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Organisation Target', {
            'fields': ('organisation_target_option',)
        }),
    )

class MobilePopulationAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Population Type', {
            'fields': ('mobile_population_type',)
        }),
    )

# Register National Organisation models
admin.site.register(NationalOrganisation)

# Register StakeHolder models
admin.site.register(StakeholderDirectory, StakeholderDirectoryAdmin)

# Register HIV Activities Organisation Participates in
admin.site.register(ActivityReportForm, ActivityReportFormAdmin)

admin.site.register(OrganisationTarget)

admin.site.register(MobilePopulation)

admin.site.register(SupportField)

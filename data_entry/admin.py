from django import forms
from django.contrib import admin

from .models import (NationalOrganisation, ActivityReportForm, StakeholderDirectory, Province, District, Ward,
OrganisationTarget, MobilePopulationType, SupportField, ProgramActivity, FundingSource, TargetGroupPreventionMessage,
OtherQuestion, EndOfYearQuestion, GeneralComment)

from .models import (IECMaterial, IECMaterial2, Teachers, OutOfSchool, SexWorker, Inmate, PersonsWithDisabilty, 
MobileWorker,MobilePopulation, MenWithMen, TransgenderIndividual, PeopleWhoInjectDrug, CondomProgramming, 
CondomProgramming2, ReportedCase, ExperiencedPhysicalViolence, ExperiencedSexualViolence, PostExposureProphylaxis,
PreExposureProphylaxis, SynergyDevelopmentSector, SupportGroupSetUp, IndividualCurrentlyEnrolled, VulnerablePeople, 
SupportAndCare, GeneralComment2)

from .forms import StakeholderDirectoryModelForm, ProgramActivityModelForm, TargetGroupPreventionMessageModelForm, \
WardModelForm

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
    verbose_name_plural = '1. how many Information Education Communication(IEC) materials were distributed by \
        your organisation this quarter?'
    extra = 1

class MaterialInline2(admin.TabularInline):
    model = IECMaterial2
    verbose_name = 'IEC Material 2'
    verbose_name_plural = '2. If you distributed Information Education Communication(IEC) materials this \
        quarter who was your target audience?'
    extra = 1

class TeachersInline(admin.TabularInline):
    model = Teachers
    verbose_name_plural = '3. Number of teachers who have received training, and taught lessons, in life \
        skills based comprehensive sexuality eduaction this quarter'
    extra = 1

class OutOfSchoolInline(admin.TabularInline):
    model = OutOfSchool
    verbose_name_plural = '4. Number of Out of School children and young people aged 10-24 years provided \
        with life skills- based comprehensive sexuality education within this quarter'
    extra = 1

class SexWorkerInline(admin.TabularInline):
    model = SexWorker
    verbose_name_plural = '5. How many sex workers were reached with HIV prevention programmes by your \
        organisation this quarter?'
    fields = ( 'sex_workers_female_10_14', 'sex_workers_female_15_19', 'sex_workers_female_20_24', 
        'sex_workers_female_25_29', 'sex_workers_female_30_34', 'sex_workers_female_35_plus', 
        'sex_workers_male_10_14','sex_workers_male_15_19', 'sex_workers_male_20_24', 'sex_workers_male_25_29', 
        'sex_workers_male_30_34', 'sex_workers_male_35_plus' )
    extra = 1

class InmateInline(admin.TabularInline):
    model = Inmate
    verbose_name_plural = '6. How many inmates were reached with HIV prevention programmes by your organisation \
        this quarter?'
    extra = 1

class PersonsWithDisabiltyInline(admin.TabularInline):
    model = PersonsWithDisabilty
    verbose_name_plural = '7. How many persons with disability were reached with HIV prevention programmes by your \
        organisation this quarter?'
    extra = 1

class MobileWorkerInline(admin.TabularInline):
    model = MobileWorker
    verbose_name_plural = '8. How many mobile workers were reached with HIV prevention programmes by your organisation \
        this quarter?'
    extra = 1

class MobilePopulationInline(admin.TabularInline):
    model = MobilePopulation
    verbose_name_plural = '9. Which types of mobile populations did your organisation reach this quarter?'
    extra = 1
    
class MenWithMenInline(admin.TabularInline):
    model = MenWithMen
    verbose_name_plural = '10. How many men who have sex with men (MSM) were reached with HIV prevention programmes by \
        your organisation this quarter?'
    extra = 1

class TransgenderIndividualInline(admin.TabularInline):
    model = TransgenderIndividual
    verbose_name_plural = '11. How many transgender individuals were reached with HIV prevention programmes by your \
        organisation this quarter?'
    extra = 1

class PeopleWhoInjectDrugInline(admin.TabularInline):
    model = PeopleWhoInjectDrug
    verbose_name_plural = '12. How many people who inject drugs(PWID) have been reached by HIV prevention programmes by \
        your organisation this quarter?'
    extra = 1

class CondomProgrammingInline(admin.TabularInline):
    model = CondomProgramming
    verbose_name_plural = '13. How many condom service distribution points were supplied by your organisation this \
        quarter(excluding health facilities)?'
    extra = 1

class CondomProgramming2Inline(admin.TabularInline):
    model = CondomProgramming2
    verbose_name_plural = '14. How many male and/or female condoms were distributed to end users by \
        your organisation this quarter(excluding health facilities)?'
    extra = 1

class ReportedCaseInline(admin.TabularInline):
    model = ReportedCase
    verbose_name_plural = '15. What is the total number of reported cases on a physical or sexual violence OR any \
        other type of gender based violence by your organisation'
    extra = 1
    
class ExperiencedPhysicalViolenceInline(admin.TabularInline):
    model = ExperiencedPhysicalViolence
    verbose_name_plural = '16. How many individuals experienced physical violence this quarter?'
    extra = 1

class ExperiencedSexualViolenceInline(admin.TabularInline):
    model = ExperiencedSexualViolence
    verbose_name_plural = '17. How many individuals experienced sexual violence this quarter?'
    extra = 1

class PostExposureProphylaxisInline(admin.TabularInline):
    model = PostExposureProphylaxis
    verbose_name_plural = '18. How many individuals who experienced physical or sexual violence were referred for \
        post exposure prophylaxis(PEP) within 72 hours in accordance with national guidelines this quarter?'
    extra = 1

class PreExposureProphylaxisInline(admin.TabularInline):
    model = PreExposureProphylaxis
    verbose_name_plural = '19. How many individuals were referred for pre-exposure prophylaxis(PrEP) by your \
        organisation this quarter?'
    extra = 1

class SynergyDevelopmentSectorInline(admin.TabularInline):
    model = SynergyDevelopmentSector
    verbose_name_plural = '20. How many employees were reached through workplace programmes by your organisation this quarter?'
    extra = 1

class SupportGroupSetUpInline(admin.TabularInline):
    model = SupportGroupSetUp
    verbose_name_plural = '21. How many support groups/ clubs/ after school groups were set up by your \
        organisation this quarter?'
    extra = 1

class IndividualCurrentlyEnrolledInline(admin.TabularInline):
    model = IndividualCurrentlyEnrolled
    verbose_name_plural = '22. How many individuals are currently enrolled and active in support groups/ clubs/ \
        after school groups set up by your organisation?'
    extra = 1

class VulnerablePeopleInline(admin.TabularInline):
    model = VulnerablePeople
    verbose_name_plural = '23. How many vulnerable people received care and support from your organisation this quarter?'
    extra = 1

class SupportAndCareInline(admin.TabularInline):
    model = SupportAndCare
    verbose_name_plural = '24. What types of care and support does your organisation provide? (select all that apply)'
    extra = 1

class GeneralComment2Inline(admin.TabularInline):
    model = GeneralComment2
    verbose_name = 'General comment'
    extra = 1

# ADMIN CLASSES
# *************************************************
class StakeholderDirectoryAdmin(admin.ModelAdmin):
    list_filter = ('national_organisation', 'organisation_province', 'district', )
    list_display = ('organisation', 'key_contact_name', 'telephone_number', 'start_year')

    form = StakeholderDirectoryModelForm

    MenWithMenInline.max_num = 1
    TeachersInline.max_num = 1
    CondomProgrammingInline.max_num = 1
    ReportedCaseInline.max_num = 1
    SynergyDevelopmentSectorInline.max_num = 1
    MenWithMenInline.max_num = 1
    CondomProgrammingInline.max_num = 1
    ReportedCaseInline.max_num = 1
    SynergyDevelopmentSectorInline.max_num = 1
    OtherQuestionInline.max_num = 1
    EndOfYearQuestionInline.max_num = 1
    GeneralCommentInline.max_num = 1
    
    fieldsets = (
        ('Basic details on the organisation', {
            #'classes':('collapse',),
            'fields': ('national_organisation','organisation', ('organisation_province', 'district'), 
            'organisation_address', 'start_year', 'gps', 'website', 'description_of_organisation')
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
        ('Organisation classification', {
            'fields': ('organisation_type', 'organisation_targets')
        })
    )

    inlines = [ProgramActivityInline, FundingSourceInline, TargetGroupPreventionMessageInline,
        OtherQuestionInline, EndOfYearQuestionInline, GeneralCommentInline]

    class Media:
        css = { "all" : ("css/hide_admin_original.css",) }

class ActivityReportFormAdmin(admin.ModelAdmin):
    list_display = ('stake_holder_name', 'quarter_been_reported')
    
    MaterialInline2.max_num = 1
    PeopleWhoInjectDrugInline.max_num = 1
    OutOfSchoolInline.max_num = 1
    SexWorkerInline.max_num = 1
    InmateInline.max_num = 1
    TransgenderIndividualInline.max_num = 1
    PersonsWithDisabiltyInline.max_num = 1
    MobileWorkerInline.max_num = 1
    MobilePopulationInline.max_num = 1
    MenWithMenInline.max_num = 1
    CondomProgrammingInline.max_num = 1
    CondomProgramming2Inline.max_num = 1
    ReportedCaseInline.max_num = 1
    ExperiencedPhysicalViolenceInline.max_num = 1
    ExperiencedSexualViolenceInline.max_num = 1
    PostExposureProphylaxisInline.max_num = 1
    PreExposureProphylaxisInline.max_num = 1
    SynergyDevelopmentSectorInline.max_num = 1
    SupportGroupSetUpInline.max_num = 1
    IndividualCurrentlyEnrolledInline.max_num = 1
    VulnerablePeopleInline.max_num = 1
    SupportAndCareInline.max_num = 1
    GeneralComment2Inline.max_num = 1

    fieldsets = (
        ('1. REPORT DETAIL', {
            'fields':('report_date', 'quarter_been_reported', 'stake_holder_name', 
                ('name', 'telephone_number', 'email_address')
            ),
        }),
        ('2. HIV ACTIVITIES YOUR ORGANISATION PARTICIPATES', {
            'fields': (),
        }),
    )

    inlines = [MaterialInline, MaterialInline2, TeachersInline, OutOfSchoolInline, SexWorkerInline, InmateInline, 
        PersonsWithDisabiltyInline, MobileWorkerInline, MobilePopulationInline, MenWithMenInline, TransgenderIndividualInline, 
        PeopleWhoInjectDrugInline,CondomProgrammingInline, CondomProgramming2Inline, ReportedCaseInline, 
        ExperiencedPhysicalViolenceInline, ExperiencedSexualViolenceInline, PostExposureProphylaxisInline, 
        PreExposureProphylaxisInline, SynergyDevelopmentSectorInline, SupportGroupSetUpInline, 
        IndividualCurrentlyEnrolledInline, VulnerablePeopleInline, SupportAndCareInline, GeneralComment2Inline]

    class Media:
        css = { "all" : ("css/hide_admin_original.css",) }

class OrganisationTargetAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Organisation Target', {
            'fields': ('organisation_target_option',)
        }),
    )

class MobilePopulationTypeAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Population Type', {
            'fields': ('mobile_population_type',)
        }),
    )

class DistrictAdmin(admin.ModelAdmin):
    list_filter = ['province',]

class WardAdmin(admin.ModelAdmin):
    list_filter = ['district',]
    form = WardModelForm

# Register National Organisation models
admin.site.register(NationalOrganisation)

# Register StakeHolder models
admin.site.register(StakeholderDirectory, StakeholderDirectoryAdmin)

# Register HIV Activities Organisation Participates in
admin.site.register(ActivityReportForm, ActivityReportFormAdmin)

# Register OrganisationTarget to enable user to add more groups that they target
admin.site.register(OrganisationTarget)

# Register MobilePopulationType to enable adding of types of workers
admin.site.register(MobilePopulationType)

# Register to add types of support under Program activities (ie, Program activities by geographic area)
admin.site.register(SupportField)

admin.site.register(Province)

admin.site.register(District, DistrictAdmin)

admin.site.register(Ward, WardAdmin)
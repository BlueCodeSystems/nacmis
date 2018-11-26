from django import forms
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.db.models import Q
from collections import OrderedDict
from django.forms import ValidationError

from .models import (NationalOrganisation, ActivityReportForm, StakeholderDirectory, Province, District, Ward,
OrganisationTarget, PreventionMessageList, MobilePopulationType, SupportField, SupportByArea, ProgramActivity, 
FundingSource, TargetGroupPreventionMessage, OtherQuestion, EndOfYearQuestion, GeneralComment, UserProfile, 
StakeholderDirectoryStaff)

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext, gettext_lazy as _

from .models import (IECMaterial, IECMaterial2, Teachers, OutOfSchool, SexWorker, Inmate, PersonsWithDisabilty, 
MobileWorker,MobilePopulation, MenWithMen, SourcesOfInformation, TransgenderIndividual, PeopleWhoInjectDrug, CondomProgramming, 
CondomProgramming2, ReportedCase, ExperiencedPhysicalViolence, ExperiencedSexualViolence, PostExposureProphylaxis,
PreExposureProphylaxis, SynergyDevelopmentSector, SupportGroupSetUp, IndividualCurrentlyEnrolled, VulnerablePeople, 
SupportAndCare, GeneralComment2, StakeholderVerification, DACAValidation, PITMEOValidation, SubheaderLabel1, 
SubheaderLabel2, SubheaderLabel3, SubheaderLabel4, SubheaderLabel5, SubheaderLabel6, SubheaderLabel7)

from .forms import ActivityReportFormModelForm, StakeholderDirectoryModelForm, ProgramActivityModelForm, \
TargetGroupPreventionMessageModelForm, WardModelForm, UserProfileModelForm, OtherQuestionModelForm, \
DACAValidationForm, PITMEOValidationForm

import datetime

# INLINES FOR STAKEHOLDER DIRECTORY ADMIN
# *************************************************
class ProgramActivityInline(admin.TabularInline):
    model = ProgramActivity
    verbose_name_plural = 'Section 5: Geographic activities'
    form = ProgramActivityModelForm
    extra = 1
    template = 'admin/tabular.html'

class FundingSourceInline(admin.TabularInline):
    model = FundingSource
    verbose_name_plural = 'Section 6: Funding sources'
    extra = 1
    template = 'admin/tabular.html'

class TargetGroupPreventionMessageInline(admin.TabularInline):
    model = TargetGroupPreventionMessage
    verbose_name_plural = 'Section 7: Target group and prevention messages'
    form = TargetGroupPreventionMessageModelForm
    extra = 1
    template = 'admin/tabular.html'

class OtherQuestionInline(admin.TabularInline):
    model = OtherQuestion
    form = OtherQuestionModelForm
    verbose_name_plural = 'Section 8: Other questions'
    extra = 1
    template = 'admin/tabular.html'

class EndOfYearQuestionInline(admin.TabularInline):
    model = EndOfYearQuestion
    verbose_name_plural = 'Section 9: End of year questions'
    extra = 1

class GeneralCommentInline(admin.StackedInline):
    model = GeneralComment
    extra = 1


class DACAValidationInline(admin.StackedInline):
    model = DACAValidation
    #form = DACAValidationForm
    extra = 1
    fields = ("validated_by", "validation_status", "acknowledgement", "daca_initials", "validation_comment")
    readonly_fields = ("acknowledgement",)
    verbose_name = 'DACA Validation'
    verbose_name_plural = 'DACA Validation'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.user.is_superuser:
            return super().formfield_for_foreignkey(db_field, request, **kwargs)

        if db_field.name == "validated_by":
            if request.user.groups.filter(name="DACA"):
                kwargs["queryset"] = User.objects.filter(id=request.user.id)
            else:
                kwargs["queryset"] = User.objects.none()

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class PITMEOValidationInline(admin.StackedInline):
    model = PITMEOValidation
    #form = PITMEOValidationForm
    extra = 1
    fields = ("validated_by", "validation_status", "acknowledgement", "pitmeo_initials", "validation_comment")
    readonly_fields = ("acknowledgement",)
    verbose_name = 'PITMEO Validation'
    verbose_name_plural = 'PITMEO Validation'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.user.is_superuser:
            return super().formfield_for_foreignkey(db_field, request, **kwargs)

        if db_field.name == "validated_by":
            if request.user.groups.filter(name="PITMEO"):
                kwargs["queryset"] = User.objects.filter(id=request.user.id)
            else:
                kwargs["queryset"] = User.objects.none()

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

# INLINES FOR ACTIVITY REPORT FORM ADMIN
# *************************************************
class MaterialInline(admin.TabularInline):
    model = IECMaterial
    verbose_name = 'IEC Material'
    verbose_name_plural = '1. How many Information Education Communication (IEC) materials were distributed by \
        your organisation this quarter?'
    extra = 1
    template = 'admin/tabular.html'

class MaterialInline2(admin.TabularInline):
    model = IECMaterial2
    verbose_name = 'IEC Material 2'
    verbose_name_plural = '2. If you distributed Information Education Communication (IEC) materials this \
        quarter who was your target audience?'
    filter_horizontal = ('target_audience',)
    can_delete = False
    extra = 1
    template = 'admin/tabular.html'

class TeachersInline(admin.TabularInline):
    model = Teachers
    verbose_name_plural = '3. Number of CSE trained teachers who taught lessons, in life skills based \
        comprehensive sexuality education(CSE) this quarter'
    can_delete = False
    template = 'admin/tabular.html'
    extra = 1

class OutOfSchoolInline(admin.StackedInline):
    model = OutOfSchool
    verbose_name_plural = '4. Number of Out of School children and young people aged 10-24 years provided \
        with life skills- based comprehensive sexuality education within this quarter'
    fields = ( ('out_school_female_10_14', 'out_school_female_15_19', 'out_school_female_20_24'), 
        ('out_school_male_10_14', 'out_school_male_15_19', 'out_school_male_20_24') 
    )
    extra = 1
    template = 'admin/stacked.html'

class SexWorkerInline(admin.StackedInline):
    model = SexWorker
    verbose_name_plural = '5. How many sex workers were reached with HIV prevention programmes by your \
        organisation this quarter?'
    fields = (  ('sex_workers_female_10_14', 'sex_workers_female_15_19', 'sex_workers_female_20_24', \
        'sex_workers_female_25_29', 'sex_workers_female_30_34', 'sex_workers_female_35_plus'), 
        ('sex_workers_male_10_14','sex_workers_male_15_19', 'sex_workers_male_20_24', 'sex_workers_male_25_29', 
        'sex_workers_male_30_34', 'sex_workers_male_35_plus') )
    extra = 1
    template = 'admin/stacked.html'

class InmateInline(admin.TabularInline):
    model = Inmate
    verbose_name_plural = '6. How many inmates were reached with HIV prevention programmes by your organisation \
        this quarter?'
    can_delete = False
    extra = 1
    template = 'admin/tabular.html'

class PersonsWithDisabiltyInline(admin.TabularInline):
    model = PersonsWithDisabilty
    verbose_name_plural = '7. How many persons with disability were reached with HIV prevention programmes by your \
        organisation this quarter?'
    can_delete = False
    extra = 1
    template = 'admin/tabular.html'

class MobileWorkerInline(admin.TabularInline):
    model = MobileWorker
    verbose_name_plural = '8. How many mobile workers were reached with HIV prevention programmes by your organisation \
        this quarter?'
    can_delete = False
    extra = 1
    template = 'admin/tabular.html'

class MobilePopulationInline(admin.TabularInline):
    model = MobilePopulation
    verbose_name_plural = '9. Which types of mobile populations did your organisation reach this quarter?'
    filter_horizontal = ('mobile_population_types',)
    can_delete = False
    extra = 1
    template = 'admin/tabular.html'
    
class MenWithMenInline(admin.TabularInline):
    model = MenWithMen
    verbose_name_plural = '10. How many men who have sex with men (MSM) were reached with HIV prevention programmes by \
        your organisation this quarter?'
    can_delete = False
    extra = 1
    template = 'admin/tabular.html'

class TransgenderIndividualInline(admin.TabularInline):
    model = TransgenderIndividual
    verbose_name_plural = '11. How many transgender individuals were reached with HIV prevention programmes by your \
        organisation this quarter?'
    can_delete = False
    extra = 1
    template = 'admin/tabular.html'

class PeopleWhoInjectDrugInline(admin.TabularInline):
    model = PeopleWhoInjectDrug
    verbose_name_plural = '12. How many people who inject drugs (PWID) have been reached by HIV prevention programmes by \
        your organisation this quarter?'
    can_delete = False
    extra = 1
    template = 'admin/tabular.html'

class CondomProgrammingInline(admin.TabularInline):
    model = CondomProgramming
    verbose_name_plural = '13. How many condom service distribution points were supplied by your organisation this \
        quarter (excluding health facilities)?'
    can_delete = False
    extra = 1
    template = 'admin/tabular.html'

class CondomProgramming2Inline(admin.TabularInline):
    model = CondomProgramming2
    verbose_name_plural = '14. How many male and/or female condoms were distributed to end users by \
        your organisation this quarter (excluding health facilities)?'
    can_delete = False
    extra = 1
    template = 'admin/tabular.html'

class ReportedCaseInline(admin.StackedInline):
    model = ReportedCase
    verbose_name_plural = '15. What is the total number of reported cases on a physical or sexual violence OR any \
        other type of gender based violence by your organisation?'
    fields = ( ('reported_female_less_10', 'reported_female_10_14', 'reported_female_15_19', 
        'reported_female_20_24', 'reported_female_25_plus'), 
        ('reported_male_less_10', 'reported_male_10_14', 'reported_male_15_19', 'reported_male_20_24', 
        'reported_male_25_plus') )
    extra = 1
    template = 'admin/stacked.html'
    
class ExperiencedPhysicalViolenceInline(admin.StackedInline):
    model = ExperiencedPhysicalViolence
    verbose_name_plural = '16. How many individuals experienced physical violence this quarter?'
    fields = ( ('physical_female_less_10', 'physical_female_10_14', 
        'physical_female_15_19', 'physical_female_20_24', 'physical_female_25_plus'), 
        ('physical_male_less_10', 'physical_male_10_14', 'physical_male_15_19', 
        'physical_male_20_24', 'physical_male_25_plus') )
    extra = 1
    template = 'admin/stacked.html'

class ExperiencedSexualViolenceInline(admin.StackedInline):
    model = ExperiencedSexualViolence
    verbose_name_plural = '17. How many individuals experienced sexual violence this quarter?'
    fields = ( ('sexual_female_less_10', 'sexual_female_10_14', 'sexual_female_15_19',
        'sexual_female_20_24', 'sexual_female_25_plus'),
        ('sexual_male_less_10', 'sexual_male_10_14', 'sexual_male_15_19', 'sexual_male_20_24', 'sexual_male_25_plus') )
    extra = 1
    template = 'admin/stacked.html'

class PostExposureProphylaxisInline(admin.StackedInline):
    model = PostExposureProphylaxis
    verbose_name_plural = '18. How many individuals who experienced physical or sexual violence were referred for \
        post exposure prophylaxis(PEP) within 72 hours in accordance with national guidelines this quarter?'
    fields = ( ('accessed_pep_female_less_10', 'accessed_pep_female_10_14', 'accessed_pep_female_15_19', 
        'accessed_pep_female_20_24', 'accessed_pep_female_25_plus'), 
        ('accessed_pep_male_less_10', 'accessed_pep_male_10_14', 'accessed_pep_male_15_19', 'accessed_pep_male_20_24', 
        'accessed_pep_male_25_plus') )
    extra = 1
    template = 'admin/stacked.html'

class PreExposureProphylaxisInline(admin.StackedInline):
    model = PreExposureProphylaxis
    verbose_name_plural = '19. How many individuals were referred for pre-exposure prophylaxis(PrEP) by your \
        organisation this quarter?'
    fields = ( ('referred_pep_female_15_19', 'referred_pep_female_20_24', 'referred_pep_female_25_plus'), 
        ('referred_pep_male_15_19', 'referred_pep_male_20_24', 'referred_pep_male_25_plus'), )
    extra = 1
    template = 'admin/stacked.html'

class SynergyDevelopmentSectorInline(admin.TabularInline):
    model = SynergyDevelopmentSector
    verbose_name_plural = '20. How many employees were reached through workplace programmes by your organisation this quarter?'
    can_delete = False
    extra = 1
    template = 'admin/tabular.html'

class SupportGroupSetUpInline(admin.TabularInline):
    model = SupportGroupSetUp
    verbose_name_plural = '21. How many support groups/ clubs/ after school groups set up by your organisation were \
        active this quarter?'
    can_delete = False
    extra = 1
    template = 'admin/tabular.html'

class IndividualCurrentlyEnrolledInline(admin.StackedInline):
    model = IndividualCurrentlyEnrolled
    verbose_name_plural = '22. How many individuals are currently enrolled in support groups/ clubs/ after school \
        groups set up by your organisation this quarter?'
    fields = ( ('individuals_enrolled_female_10_14', 'individuals_enrolled_female_15_19', 
        'individuals_enrolled_female_20_24', 'individuals_enrolled_female_25_plus'), 
        ('individuals_enrolled_male_10_14', 'individuals_enrolled_male_15_19', 'individuals_enrolled_male_20_24', 
        'individuals_enrolled_male_25_plus') )
    extra = 1
    template = 'admin/stacked.html'

class VulnerablePeopleInline(admin.StackedInline):
    model = VulnerablePeople
    verbose_name_plural = '23. How many vulnerable people received care and support from your organisation this quarter?'
    fields = ( ('ovc_female_less_10', 'ovc_female_10_14', 'ovc_female_15_19', 'ovc_female_20_24', 
        'ovc_female_25_plus'), ('ovc_male_less_10', 'ovc_male_10_14', 'ovc_male_15_19', 'ovc_male_20_24', 'ovc_male_25_plus') )
    extra = 1
    template = 'admin/stacked.html'

class SupportAndCareInline(admin.TabularInline):
    model = SupportAndCare
    verbose_name_plural = '24. What types of care and support does your organisation provide? (select all that apply)'
    filter_horizontal = ('type',)
    can_delete = False
    extra = 1
    template = 'admin/tabular.html'

class GeneralComment2Inline(admin.StackedInline):
    model = GeneralComment2
    verbose_name = 'General comment'
    extra = 1

class StakeholderVerificationInline(admin.StackedInline):
    model = StakeholderVerification
    readonly_fields = ("acknowledgement",)
    fields = ( 'acknowledgement', 'stakeholder_initials' )

# Inlines for the subsection headers
class SubheaderLabel1Inline(admin.StackedInline):
    model = SubheaderLabel1
    verbose_name_plural = 'SOCIAL BEHAVIOUR CHANGE COMMUNICATION'

class SubheaderLabel2Inline(admin.StackedInline):
    model = SubheaderLabel2
    verbose_name_plural = 'SOCIAL BEHAVIOUR CHANGE COMMUNICATION FOR KEY POPULATIONS'

class SubheaderLabel3Inline(admin.StackedInline):
    model = SubheaderLabel3
    verbose_name_plural = 'CONDOM PROGRAMMING'

class SubheaderLabel4Inline(admin.StackedInline):
    model = SubheaderLabel4
    verbose_name_plural = 'CRITICAL ENABLERS'

class SubheaderLabel5Inline(admin.StackedInline):
    model = SubheaderLabel5
    verbose_name_plural = 'SYNERGIES WITH OTHER DEVELOPMENT SECTORS'

class SubheaderLabel6Inline(admin.StackedInline):
    model = SubheaderLabel6
    verbose_name_plural = 'COMMUNITY HEALTH SYSTEMS'

class SubheaderLabel7Inline(admin.StackedInline):
    model = SubheaderLabel7
    verbose_name_plural = 'BELOW SECTION TO BE FILLED BY DACA / LOCAL AUTHORITY ONLY'

# ADMIN CLASSES
# *************************************************
class StakeholderDirectoryAdmin(admin.ModelAdmin):
    list_filter = ('organisation_province', 'organisation_district', )
    list_display = ('organisation', 'key_contact_name', 'telephone_number',)
    filter_horizontal = ('position_available',)

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

    fieldsets = (
        ('Section 1: Basic details on the organisation', {
            #'classes':('collapse',),
            'fields': ('national_organisation','organisation', ('organisation_province', 'organisation_district'), 
            'organisation_address', 'start_year', 'gps', 'website', 'description_of_organisation')
        }),
        ('Section 2: Contact details', {
            'fields': ('key_contact_name', 'position_within_organisation', 'telephone_number', 
            'telephone_number_alternative', 'email_address'),
        }),
        ('Section 3: Staff details', {
            'fields': ( ('permanent_employee_male', 'permanent_employee_female'), ('temporary_employee_male', 
                'temporary_employee_female'), ('volunteer_employee_male', 'volunteer_employee_female'), 
                'position_available' ),
                
                'description':('<b><p class="description_fit_in">Employee\'s fall in different groups. Permanent employees \
                are those who is hired to work without any time frame for his/her exit. Temporary employees are those that \
                are hired for a limited period of time. <br/>They are usually hired on a casual, part-time, or full-time \
                basis, but the employment is temporary. Volunteer employees donate their time and energy without receiving \
                financial gain. These employees <br/>usually do not displace any other employee types and usually not \
                entitled to many benefits as compared to other employee types.</p></b>'),
        }),
        ('Section 4: Organisation classification', {
            'fields': ( ('organisation_type', 'other_organisation_type'), ('organisation_targets', 'other_organisation_target') )
        })
    )

    # exclude inlines OtherQuestionInline, EndOfYearQuestionInline by default
    inlines = [ProgramActivityInline, FundingSourceInline, TargetGroupPreventionMessageInline, GeneralCommentInline]

    current_year = datetime.datetime.now().strftime("%Y")
    current_month = datetime.datetime.now().strftime("%m")
    
    if( int(current_month) < 4 ):
        endlist = []
        endlist.append(inlines.pop()) #append the last element to a new list
        
        inlines.extend([OtherQuestionInline, EndOfYearQuestionInline])
        inlines.extend(endlist)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        
        if request.user.is_superuser:
            return super().formfield_for_foreignkey(db_field, request, **kwargs)

        if db_field.name == "organisation_province":
            try:
                userProfile = UserProfile.objects.get(user=request.user)
            except UserProfile.DoesNotExist:
                #No userprofile set, return empty queryset
                kwargs["queryset"] = Province.objects.none()
            else: 
                if request.user.groups.filter(name="DACA"):
                    kwargs["queryset"] = Province.objects.filter(name=userProfile.province)
                if request.user.groups.filter(name="PACA"):
                    kwargs["queryset"] = Province.objects.filter(name=userProfile.province)
                if request.user.groups.filter(name="PITMEO"):
                    kwargs["queryset"] = Province.objects.filter(name=userProfile.province)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        try:
            userProfile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            #No userprofile set, return empty queryset
            return qs.none()
        else: 
            if request.user.groups.filter(name="Stakeholder"):
                try:
                    qs = qs.filter(id=userProfile.stakeholder.id)
                except AttributeError:
                    qs = qs.none()
            if request.user.groups.filter(name="DACA"):
                qs = qs.filter(organisation_district=userProfile.district)
            if request.user.groups.filter(name="PITMEO"):
                qs = qs.filter(organisation_province=userProfile.province)
        return qs

    class Media:
        css = { "all" : ("css/hide_admin_original.css",) }

def pitmeo_validation_status(obj):
    label = ''
    try:
        label = "%s"%obj.pitmeovalidation_set.all()[0].validation_status
    except IndexError:
        pass
    return label.upper()

def daca_validation_status(obj):
    label = ''
    try:
        label = "%s"%obj.dacavalidation_set.all()[0].validation_status
    except IndexError:
        pass
    return label.upper()

class ActivityReportFormAdmin(admin.ModelAdmin):
    form =  ActivityReportFormModelForm
    list_display = ('stake_holder_name', 'name', daca_validation_status, pitmeo_validation_status, 'quarter_been_reported')
    list_filter = ('stake_holder_name__organisation_province__name', 'quarter_been_reported', 'dacavalidation__validation_status', 
        'pitmeovalidation__validation_status', 'stake_holder_name__organisation_district__name',)
    search_fields = ['stake_holder_name__organisation']

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
    StakeholderVerificationInline.max_num = 1
    DACAValidationInline.max_num = 1
    PITMEOValidationInline.max_num = 1
    GeneralCommentInline.max_num = 1
    SubheaderLabel1Inline.max_num = 1
    SubheaderLabel2Inline.max_num = 1
    SubheaderLabel3Inline.max_num = 1
    SubheaderLabel4Inline.max_num = 1
    SubheaderLabel5Inline.max_num = 1
    SubheaderLabel6Inline.max_num = 1
    SubheaderLabel7Inline.max_num = 1

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

    inlines = [SubheaderLabel1Inline, MaterialInline, MaterialInline2, SubheaderLabel2Inline, TeachersInline, OutOfSchoolInline, 
        SexWorkerInline, InmateInline, PersonsWithDisabiltyInline, MobileWorkerInline, MobilePopulationInline, MenWithMenInline, 
        TransgenderIndividualInline, PeopleWhoInjectDrugInline, SubheaderLabel3Inline, CondomProgrammingInline, 
        CondomProgramming2Inline, SubheaderLabel4Inline, ReportedCaseInline, ExperiencedPhysicalViolenceInline, 
        ExperiencedSexualViolenceInline, PostExposureProphylaxisInline, PreExposureProphylaxisInline, SubheaderLabel5Inline, 
        SynergyDevelopmentSectorInline, SubheaderLabel6Inline, SupportGroupSetUpInline, IndividualCurrentlyEnrolledInline, 
        VulnerablePeopleInline, SupportAndCareInline, GeneralComment2Inline, StakeholderVerificationInline, SubheaderLabel7Inline, 
        DACAValidationInline, PITMEOValidationInline]

    """
    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
ActivityReportForm
        readonly_fields = (
            list(readonly_fields) +
            [field.name for field in self.opts.fields
                if field.editable] +
            [field.name for field in self.opts.many_to_many
                if field.editable]
        )

        # remove duplicates whilst preserving order
        readonly_fields = list(OrderedDict.fromkeys(readonly_fields))

        # Remove from the readonly_fields list the excluded fields
        # specified on the form or the modeladmin
        excluded_fields = self.get_excluded_fields()
        if excluded_fields:
            readonly_fields = [
                f for f in readonly_fields if f not in excluded_fields
            ]
        #Also mark inlines as readonly
        for inline in self.inlines:
            print(inline.opts)

        return tuple(readonly_fields)
        """

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.user.is_superuser:
            if db_field.name == "stake_holder_name":
                kwargs["queryset"] = StakeholderDirectory.objects.order_by('organisation')   
            return super().formfield_for_foreignkey(db_field, request, **kwargs)

        stakeholders = StakeholderDirectory.objects.order_by('organisation')
        #stakeholders = StakeholderDirectory.objects.all()
        if db_field.name == "stake_holder_name":
            try:
                userProfile = UserProfile.objects.get(user=request.user)
            except UserProfile.DoesNotExist:
                #No userprofile set, return empty queryset
                kwargs["queryset"] = stakeholders.none()
            else: 
                if request.user.groups.filter(name="PACA"):
                    kwargs["queryset"] = stakeholders.filter(organisation_province=userProfile.province)
                if request.user.groups.filter(name="PITMEO"):
                    kwargs["queryset"] = stakeholders.filter(organisation_province=userProfile.province)
                if request.user.groups.filter(name="DACA"):
                    kwargs["queryset"] = stakeholders.filter(organisation_district=userProfile.district)
                if request.user.groups.filter(name="Stakeholder"):
                    kwargs["queryset"] = stakeholders.filter(id=userProfile.stakeholder.id)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        try:
            userProfile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            return qs.none()
        else: 
            if request.user.groups.filter(name="Stakeholder"):
                qs = qs.filter(stake_holder_name=userProfile.stakeholder)
            if request.user.groups.filter(name="DACA"):
                qs = qs.filter(stake_holder_name__organisation_district=userProfile.district)
            if request.user.groups.filter(name="PITMEO"):
                activity_form_province = qs.filter(stake_holder_name__organisation_province=userProfile.province)
                qs = activity_form_province.filter(dacavalidation__validation_status="approved")
        return qs

    class Media:
        css = { "all" : ("css/hide_admin_original.css",) }
        js = ('admin/js/hide_na_inlines.js',)

class DistrictAdmin(admin.ModelAdmin):
    list_filter = ['province',]

class WardAdmin(admin.ModelAdmin):
    list_filter = ['district',]
    search_fields = ['name']
    form = WardModelForm

class NationalOrganisationAdmin(admin.ModelAdmin):
    search_fields = ['organisation_name',]

#The code below is meant to include the user profile process directly into the user creation dialogue
class UserProfileInline(admin.StackedInline):
    form = UserProfileModelForm
    model = UserProfile
    can_delete = False
    verbose_name_plural = "User Profile"
    fk_name = "user"

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.user.is_superuser:
            return super().formfield_for_foreignkey(db_field, request, **kwargs)

        if db_field.name == "province":
            try:
                userProfile = UserProfile.objects.get(user=request.user)
            except UserProfile.DoesNotExist:
                #No userprofile set, return empty queryset
                kwargs["queryset"] = Province.objects.none()
            else: 
                if request.user.groups.filter(name="DACA"):
                    kwargs["queryset"] = Province.objects.filter(name=userProfile.province)
        if db_field.name == "stakeholder":
            try:
                userProfile = UserProfile.objects.get(user=request.user)
            except UserProfile.DoesNotExist:
                #No userprofile set, return empty queryset
                kwargs["queryset"] = StakeholderDirectory.objects.none()
            else: 
                if request.user.groups.filter(name="DACA"):
                    kwargs["queryset"] = StakeholderDirectory.objects.filter(organisation_district=userProfile.district)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


#Define a new user admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)

    def save_model(self, request, obj, form, change):
        super(UserAdmin, self).save_model(request, obj, form, change)
        creators_profile = UserProfile.objects.get(user=request.user)
        profile, created = UserProfile.objects.get_or_create(
            user=obj,
            defaults={'created_by':request.user, 'district':creators_profile.district, 'province':creators_profile.province}
            )
        if created:
            obj.is_active = True
            obj.is_staff = True
            #We won't put this in an error exception since it should be a very bad/fatal failure.
            obj.groups.add(Group.objects.get(name="Stakeholder"))
            obj.save()

        return super(UserAdmin, self).save_model(request, obj, form, change)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        #Filter to leave only the stakeholder group in the selection list for groups
        if request.user.is_superuser:
            return super().formfield_for_foreignkey(db_field, request, **kwargs)

        if db_field.name == "groups":
            try:
                userProfile = UserProfile.objects.get(user=request.user)
            except UserProfile.DoesNotExist:
                #No userprofile set, return empty queryset
                kwargs["queryset"] = Group.objects.none()
            else: 
                if request.user.groups.filter(name="DACA"):
                    kwargs["queryset"] = Group.objects.filter(name="Stakeholder")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        #Filter to leave only the users from a DACA's district
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        try:
            userProfile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            return qs.none()
        else: 
            if request.user.groups.filter(name="DACA"):
                qs = qs.filter(userprofile__district=userProfile.district)
                #Filter to only show stakeholder users.
                #qs = qs.filter(groups__name="Stakeholder")
        return qs

    def get_fieldsets(self, request, obj=None):
        if not obj:
            self.inlines = []#Don't add the inlines for userprofile
            return super().get_fieldsets(request, obj)
        else:
            self.inlines = (UserProfileInline,)
            #If this is a DACA, we need remove the superuser attribute from their edit page.
            if request.user.groups.filter(name="DACA"):
                self.fieldsets = (
                (_('Credentials'), {'fields': ('username', 'password')}),
                (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
                (_('Permissions'), {'fields': ('is_active', 'is_staff', 
                                                'groups')}),
                )
            else:
                self.fieldsets = (
                (None, {'fields': ('username', 'password')}),
                (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
                (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                                'groups')}),
                )
        return super().get_fieldsets(request, obj)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register National Organisation models
admin.site.register(NationalOrganisation, NationalOrganisationAdmin)

# Register StakeHolder models
admin.site.register(StakeholderDirectory, StakeholderDirectoryAdmin)

# Register HIV Activities Organisation Participates in
admin.site.register(ActivityReportForm, ActivityReportFormAdmin)

# Register OrganisationTarget to enable user to add more groups that they target
admin.site.register(OrganisationTarget)

# Register MobilePopulationType to enable adding of types of workers
admin.site.register(PreventionMessageList)

# Register MobilePopulationType to enable adding of types of workers
admin.site.register(MobilePopulationType)

# Register list to use for Question 24,the SupportAndCare model
admin.site.register(SupportField)

# Register to add types of support under Program activities (ie, Program activities by geographic area)
admin.site.register(SupportByArea)

admin.site.register(SourcesOfInformation)

admin.site.register(Province)

admin.site.register(District, DistrictAdmin)

admin.site.register(Ward, WardAdmin)

admin.site.register(StakeholderDirectoryStaff)

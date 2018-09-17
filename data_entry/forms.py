from django import forms


from .models import StakeholderDirectory, ProgramActivity, TargetGroupPreventionMessage, District, Ward, \
    UserProfile, OtherQuestion, DACAValidation, PITMEOValidation
from .models import ActivityReportForm, IECMaterial
from dal import autocomplete

class StakeholderDirectoryModelForm(forms.ModelForm):

    class Meta:
        model = StakeholderDirectory
        fields = ['national_organisation', 'organisation_address', 'organisation_targets', 'organisation_province', 
            'organisation_district', 'start_year']

        widgets = {
            'national_organisation' : autocomplete.ModelSelect2(url='national-organisation-autocomplete'),
            'organisation_address' : forms.TextInput(attrs={'placeholder':'Enter district address'}),
            'organisation_targets' : autocomplete.ModelSelect2Multiple(url='organisationtarget-autocomplete'),
            'organisation_district' : autocomplete.ModelSelect2(url='district-autocomplete', forward=['organisation_province']),
            'start_year': forms.TextInput(attrs={'placeholder':'YYYY-MM-DD',}),
        }

        """
        if (iecmaterial == True):
            if id == 'iecmaterial_set-group':
                add class to hide/ grey out div
        elif (iecmaterial2 == True):
            if id == 'iecmaterial_set-group':
                add class to hide/ grey out div
        elif (teacher == True):
            if id == 'teachers_set-group':
                add class to hide/ grey out div
        elif (outofschool == True):
            if id == 'outofschool_set-group':
                add class to hide/ grey out div
        elif (sexworker == True):
            if id == 'sexworker_set-group':
                add class to hide/ grey out div
        elif (inmate == True):
            if id == 'inmate_set-group':
                add class to hide/ grey out div
        elif (personswithdisability == True):
            if id == 'personswithdisabilty_set-group':
                add class to hide/ grey out div
        elif (mobileworker == True):
            if id == 'mobileworker_set-group':
                add class to hide/ grey out div
        elif (mobilepopulation == True):
            if id == 'mobilepopulation_set-group':
                add class to hide/ grey out div
        elif (menwithmen == True):
            if id == 'menwithmen_set-group':
                add class to hide/ grey out div
        elif (transgenderindividual == True):
            if id == 'transgenderindividual_set-group':
                add class to hide/ grey out div
        elif (peoplewhoinjectdrug == True):
            if id == 'peoplewhoinjectdrug_set-group':
                add class to hide/ grey out div
        elif (condomprogramming == True):
            if id == 'condomprogramming_set-group':
                add class to hide/ grey out div
        elif (condomprogramming2 == True):
            if id == 'condomprogramming2_set-group':
                add class to hide/ grey out div
        elif (reportedcase == True):
            if id == 'reportedcase_set-group':
                add class to hide/ grey out div
        elif (experiencedphysicalviolence == True):
            if id == 'experiencedphysicalviolence_set-group':
                add class to hide/ grey out div
        elif (experiencedsexualviolence == True):
            if id == 'experiencedsexualviolence_set-group':
                add class to hide/ grey out div
        elif (postexposureprophylaxis == True):
            if id == 'postexposureprophylaxis_set-group':
                add class to hide/ grey out div
        elif (preexposureprophylaxis == True):
            if id == 'preexposureprophylaxis_set-group':
                add class to hide/ grey out div
        elif (synergydevelopmentsector == True):
            if id == 'synergydevelopmentsector_set-group':
                add class to hide/ grey out div
        elif (supportgroupsetup == True):
            if id == 'supportgroupsetup_set-group':
                add class to hide/ grey out div
        elif (individualcurrentlyenrolled == True):
            if id == 'individualcurrentlyenrolled_set-group':
                add class to hide/ grey out div
        elif (vulnerablepeople == True):
            if id == 'vulnerablepeople_set-group':
                add class to hide/ grey out div
        elif (supportandcare == True):
            if id == 'supportandcare_set-group':
                add class to hide/ grey out div
        """
class UserProfileModelForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('__all__')

        widgets = {
            'national_organisation' : autocomplete.ModelSelect2(url='national-organisation-autocomplete', forward=['organisation_province']),
            'district' : autocomplete.ModelSelect2(url='district-autocomplete', forward=['province']),
            'stakeholder' : autocomplete.ModelSelect2(url='stakeholder-autocomplete', forward=['national_organisation']),
        }

class ActivityReportFormModelForm(forms.ModelForm):
    #quarter_been_reported = forms.CharField(choice=year_quarter_tuple(),)
    class Meta:
        model = ActivityReportForm
        fields = ['report_date',]
        
        widgets = {
            'report_date' : forms.TextInput(attrs={'placeholder':'YYYY-MM-DD', 'type':'date',}),
        }

class ProgramActivityModelForm(forms.ModelForm):
    # organisation_district
    class Meta:
        model = ProgramActivity
        fields = '__all__'
        
        widgets = {
            #'areas_of_support': autocomplete.ModelSelect2Multiple(url='supportfield-autocomplete'),
            'areas_of_support2': autocomplete.ModelSelect2Multiple(url='supportbyarea-autocomplete'),
            'ward':  autocomplete.ModelSelect2(url='ward-autocomplete', forward=['organisation_district'])
        }

class OtherQuestionModelForm(forms.ModelForm):
    class Meta:
        model = OtherQuestion
        fields = '__all__'

        widgets = {
            'sources_of_information' : autocomplete.ModelSelect2Multiple(url='supportofinformation-autocomplete'),
        }

class WardModelForm(forms.ModelForm):
    class Meta:
        model = Ward
        fields = '__all__'

        widgets = {
            'district' : autocomplete.ModelSelect2(url='district-autocomplete', forward=['organisation_province']),
        }

class TargetGroupPreventionMessageModelForm(forms.ModelForm):

    class Meta:
        model = TargetGroupPreventionMessage
        fields = '__all__'
        
        widgets = {
            'prevention_list': autocomplete.ModelSelect2(url='preventionmessagelist-autocomplete',),
            'target_groups': autocomplete.ModelSelect2Multiple(url='organisationtarget-autocomplete'),
        }

class IECMaterialModelForm(forms.ModelForm):

    class Meta:
        model = IECMaterial
        fields = '__all__'
        
        widgets = {
            'targeted_audience': autocomplete.ModelSelect2Multiple(url='organisationtarget-autocomplete'),
        }
class DACAValidationForm(forms.ModelForm):
    class Meta:
        model = DACAValidation
        fields = '__all__'
        widgets = {
            'acknowledgement': forms.Textarea(attrs={'class':'hide_acknowledgement'}),
            'daca_initials': forms.TextInput(attrs={'class':'hide_acknowledgement'})
        }

class PITMEOValidationForm(forms.ModelForm):
    class Meta:
        model = PITMEOValidation
        fields = '__all__'
        widgets = {
            'acknowledgement': forms.Textarea(attrs={'class':'hide_acknowledgement'}),
            'pitmeo_initials': forms.TextInput(attrs={'class':'hide_acknowledgement'})
        }

class MyForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
   

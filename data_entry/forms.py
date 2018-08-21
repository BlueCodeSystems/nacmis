from django import forms


from .models import StakeholderDirectory, ProgramActivity, TargetGroupPreventionMessage, District, Ward, \
    UserProfile, OtherQuestion, DACAValidation, PITMEOValidation
from .models import ActivityReportForm, IECMaterial
from dal import autocomplete

class StakeholderDirectoryModelForm(forms.ModelForm):

    class Meta:
        model = StakeholderDirectory
        fields = ['organisation_address', 'organisation_targets', 'organisation_province', 'organisation_district', 'start_year']

        widgets = {
            'organisation_address' : forms.TextInput(attrs={'placeholder':'Enter district address'}),
            'organisation_targets' : autocomplete.ModelSelect2Multiple(url='organisationtarget-autocomplete'),
            'organisation_district' : autocomplete.ModelSelect2(url='district-autocomplete', forward=['organisation_province']),
            'start_year': forms.TextInput(attrs={'placeholder':'YYYY-MM-DD',}),
        }

class UserProfileModelForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('__all__')

        widgets = {
            'district' : autocomplete.ModelSelect2(url='district-autocomplete', forward=['province']),
            'stakeholder' : autocomplete.ModelSelect2(url='stakeholder-autocomplete', forward=['national_organisation']),
        }

class ActivityReportFormModelForm(forms.ModelForm):
    quarter_been_reported = forms.CharField(choice=year_quarter_tuple(),)
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
            'areas_of_support': autocomplete.ModelSelect2Multiple(url='supportfield-autocomplete'),
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
   

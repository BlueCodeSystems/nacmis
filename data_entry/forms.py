from django import forms


from .models import StakeholderDirectory, ProgramActivity, TargetGroupPreventionMessage, District, Ward
from .models import ActivityReportForm, IECMaterial
from dal import autocomplete

class StakeholderDirectoryModelForm(forms.ModelForm):

    class Meta:
        model = StakeholderDirectory
        fields = ['organisation_address', 'organisation_targets', 'district', 'start_year']

        widgets = {
            'organisation_address' : forms.TextInput(attrs={'placeholder':'Enter district address'}),
            'organisation_targets' : autocomplete.ModelSelect2Multiple(url='organisationtarget-autocomplete'),
            'district' : autocomplete.ModelSelect2(url='district-autocomplete', forward=['organisation_province']),
            'start_year':  forms.TextInput(attrs={'placeholder':'YYYY-MM-DD', 'type':'date',}),
        }

class ActivityReportFormModelForm(forms.ModelForm):
    
    class Meta:
        model = ActivityReportForm
        fields = ['report_date',]
        
        widgets = {
            'report_date' : forms.TextInput(attrs={'placeholder':'YYYY-MM-DD',  'type':'date',}),
        }

class ProgramActivityModelForm(forms.ModelForm):
    # organisation_district
    class Meta:
        model = ProgramActivity
        fields = '__all__'
        
        widgets = {
            'area_of_support': autocomplete.ModelSelect2Multiple(url='supportfield-autocomplete'),
            'ward':  autocomplete.ModelSelect2(url='ward-autocomplete', forward=['organisation_district'])
        }

class WardModelForm(forms.ModelForm):
    class Meta:
        model = Ward
        fields = ['name',]

        widgets = {
            'name' : autocomplete.ModelSelect2(url='ward-autocomplete', forward=['district'])
        }

class TargetGroupPreventionMessageModelForm(forms.ModelForm):

    class Meta:
        model = TargetGroupPreventionMessage
        fields = '__all__'
        
        widgets = {
            'target_group': autocomplete.ModelSelect2Multiple(url='organisationtarget-autocomplete'),
        }

class IECMaterialModelForm(forms.ModelForm):

    class Meta:
        model = IECMaterial
        fields = '__all__'
        
        widgets = {
            'targeted_audience': autocomplete.ModelSelect2Multiple(url='organisationtarget-autocomplete'),
        }

class MyForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
   
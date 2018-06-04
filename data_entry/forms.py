from django import forms


from .models import StakeholderDirectory, ProgramActivity, TargetGroupPreventionMessage, District
from .models import ActivityReportForm, IECMaterial
from dal import autocomplete

class StakeholderDirectoryModelForm(forms.ModelForm):

    class Meta:
        model = StakeholderDirectory
        #fields = '__all__' # including all fields of model
        fields = ['organisation_address', 'organisation_target', 'organisation_district', 'start_year']

        widgets = {
            'organisation_address' : forms.TextInput(attrs={'placeholder':'Enter district address'}),
            'organisation_target' : autocomplete.ModelSelect2Multiple(url='organisationtarget-autocomplete'),
            'organisation_district' : autocomplete.ModelSelect2(url='district-autocomplete', forward=['organisation_province']),
            'start_year':  forms.TextInput(attrs={'placeholder':'YYYY-MM-DD'},), # might need a custom widget here
        }
    
class ActivityReportFormModelForm(forms.ModelForm):
    
    class Meta:
        model = ActivityReportForm
        fields = ['report_date',]
        
        widgets = {
            'report_date' : forms.TextInput(attrs={'placeholder':'YYYY-MM-DD'},),
        }

        field_classes = {
            #'report_date': DateYearField
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
   
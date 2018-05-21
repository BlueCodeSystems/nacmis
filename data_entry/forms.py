from django import forms


from .models import StakeholderDirectory, ProgramActivity, TargetGroupPreventionMessage, District
from .models import ActivityReportForm, IECMaterial
from dal import autocomplete

class StakeholderDirectoryModelForm(forms.ModelForm):

    class Meta:
        model = StakeholderDirectory
        #fields = '__all__' # including all fields of model
        fields = ['organisation_address', 'organisation_target', 'organisation_district']   # 'start_year',

        widgets = {
            'start_year' : forms.TextInput(attrs={'placeholder':'YYYY-MM-DD'}),
            'organisation_address' : forms.TextInput(attrs={'placeholder':'Enter district address'}),
            'organisation_target' : autocomplete.ModelSelect2Multiple(url='organisationtarget-autocomplete'),
            'organisation_district' : autocomplete.ModelSelect2(url='district-autocomplete', forward=['organisation_province']),
        }
    
class ActivityReportFormModelForm(forms.ModelForm):
    class Meta:
        model = ActivityReportForm
        fields = '__all__'
        widgets = {
            #'location_district' : autocomplete.ModelSelect2(url='district-autocomplete', forward=['location_province']),
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

    
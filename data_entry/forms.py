from django import forms


from .models import StakeholderDirectory, ProgramActivity, TargetGroupPreventionMessage
from .models import ActivityReportForm, IECMaterial
from django_select2.forms import Select2MultipleWidget
from dal import autocomplete

class StakeholderDirectoryModelForm(forms.ModelForm):  
    class Meta:
        model = StakeholderDirectory
        #fields = '__all__' # including all fields of model
        fields = ['organisation_address', 'organisation_target',]   # 'start_year', 

        widgets = {
            #'start_year' : forms.TextInput(attrs={'placeholder':'YYYY-MM-DD'}),
            'organisation_address' : forms.TextInput(attrs={'placeholder':'Enter district address'}),
            'organisation_target' : autocomplete.ModelSelect2Multiple(url='organisationtarget-autocomplete'),
        }

class ActivityReportFormModelForm(forms.ModelForm):
    class Meta:
        model = ActivityReportForm
        fields = '__all__'
        widgets = {
            'location_district' : autocomplete.ModelSelect2Multiple(url='district-autocomplete', forward=['location_province']),
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
    stakes = forms.ModelChoiceField( queryset=StakeholderDirectory.objects.all(), widget=Select2MultipleWidget)
    
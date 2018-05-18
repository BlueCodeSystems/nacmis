from django import forms


from .models import StakeholderDirectory, ProgramActivity, TargetGroupPreventionMessage
from .models import ActivityReportForm, IECMaterial
from django_select2.forms import Select2MultipleWidget
from dal import autocomplete

class StakeholderDirectoryModelForm(forms.ModelForm):

    class Meta:
        model = StakeholderDirectory
        #fields = '__all__' # including all fields of model
        fields = ['start_year', 'organisation_address', 'organisation_target',]

        widgets = {
            'start_year' : forms.TextInput(attrs={'placeholder':'YYYY-MM-DD'}),
            'organisation_address' : forms.TextInput(attrs={'placeholder':'Enter district address'}),
            'organisation_target' : autocomplete.ModelSelect2Multiple(url='organisationtarget-autocomplete'),
        }

class ProgramActivityModelForm(forms.ModelForm):

    class Meta:
        model = ProgramActivity
        fields = '__all__'
        
        widgets = {
            'area_of_support': autocomplete.ModelSelect2Multiple(url='supportfield-autocomplete'),
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
    
from django import forms


from .models import StakeholderDirectory, ProgramActivity, TargetGroupPreventionMessage
from .models import ActivityReportForm
from django_select2.forms import Select2MultipleWidget
from dal import autocomplete

class StakeholderDirectoryModelForm(forms.ModelForm):

    class Meta:
        model = StakeholderDirectory
        #fields = '__all__' # including all fields of model
        fields = ['start_year', 'organization_address', ]

        widgets = {
            'start_year' : forms.TextInput(attrs={'placeholder':'YYYY-MM-DD'}),
            'organization_address' : forms.TextInput(attrs={'placeholder':'Enter district address'}),
        }

class ProgramActivityModelForm(forms.ModelForm):

    class Meta:
        model = ProgramActivity
        fields = '__all__'
        
        widgets = {
            'area_of_support': Select2MultipleWidget,
            'area_of_support': autocomplete.ModelSelect2(url='supportfield-autocomplete'),
        }

class TargetGroupPreventionMessageModelForm(forms.ModelForm):

    class Meta:
        model = TargetGroupPreventionMessage
        fields = '__all__'
        
        widgets = {
            'target_group': Select2MultipleWidget,
        }

class MyForm(forms.Form):
    #stakes = forms.ModelChoiceField( queryset=StakeholderDirectory.objects.all(), widget=Select2MultipleWidget)
    
    stakes = forms.ModelChoiceField(queryset=StakeholderDirectory.objects.all(), 
        widget=autocomplete.ModelSelect2(url='stakeholderdirectory-autocomplete'))

    class Meta:
        model: ProgramActivity
        fields: ('__all__')
    
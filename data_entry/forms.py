from django import forms


from .models import StakeholderDirectory, ProgramActivity, TargetGroupPreventionMessage
from .models import ActivityReportForm
from django_select2.forms import Select2MultipleWidget
from dal import autocomplete

lusaka = 'Lusaka Province'
central = 'Central Province'
copperbelt = 'Copperbelt Province'
eastern = 'Easten Province'
luapula = 'Luapula Province'
muchinga = 'Muchinga Province'
north_western = 'North Westen Province'
northern = 'Northern Province'
southern = 'Southern Province'
western = 'Western Province'

PROVINCES_ZAMBIA = (
    (lusaka, 'Lusaka Province'),
    (central, 'Central Province'),
    (copperbelt, 'Copperbelt Province'),
    (eastern, 'Easten Province'),
    (luapula, 'Luapula Province'),
    (muchinga, 'Muchinga Province'),
    (north_western, 'North Westen Province'),
    (northern, 'Northern Province'),
    (southern, 'Southern Province'),
    (western, 'Western Province')
)

DISTRICTS = (
    ('Ben Kafupi', 'Ben Kafupi'),
    ('Justine Kabwe', 'Justine Kabwe'),
    ('Munyama', 'Munyama'),
    ('Ndola', 'Ndola'),
    ('Lufwanyama', 'Lufwanyama'),
    ('Mpongwe', 'Mpongwe')
)

class StakeholderDirectoryModelForm(forms.ModelForm):
    district = forms.ChoiceField(choices=DISTRICTS)

    class Meta:
        model = StakeholderDirectory
        #fields = '__all__' # including all fields of model
        fields = ['start_year', 'organization_address', 'organization_district',]

        widgets = {
            'start_year' : forms.TextInput(attrs={'placeholder':'YYYY-MM-DD'}),
            'organization_address' : forms.TextInput(attrs={'placeholder':'Enter district address'}),
            'organization_district' : autocomplete.ModelSelect2Multiple(url='district-autocomplete'), 
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
            'target_group': autocomplete.ModelSelect2Multiple(url='organizationtarget-autocomplete'),
        }

class MyForm(forms.Form):
    stakes = forms.ModelChoiceField( queryset=StakeholderDirectory.objects.all(), widget=Select2MultipleWidget)
    
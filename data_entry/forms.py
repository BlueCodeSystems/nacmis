from django import forms


from .models import StakeholderDirectory
from .models import ActivityReportForm

class StakeholderDirectoryModelForm(forms.ModelForm):

    class Meta:
        model = StakeholderDirectory
        #fields = '__all__' # including all fields of model
        fields = ['start_year', 'organization_address']

        widgets = {
            'start_year' : forms.TextInput(attrs={'placeholder':'YYYY-MM-DD'}),
            'organization_address' : forms.TextInput(attrs={'placeholder':'Enter district address'}),
        }

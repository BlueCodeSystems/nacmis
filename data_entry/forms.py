from django.forms import ModelForm

import datetime 
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import StakeholderDirectory
from .models import ActivityReportForm

class StakeholderDirectoryModelForm(ModelForm):
    'implements existing Stakeholder directory model'

    def clean_start_year(self):
        data = self.cleaned_data['start_year']

        # check if start year is in the future of current time
        if data > datetime.date.today():
            raise ValidationError(_('Invalid date - start date can not be after currrent date') )

        return data

    class Meta:
        model = StakeholderDirectory
        fields = ['start_year']

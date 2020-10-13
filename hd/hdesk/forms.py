from django.forms import ModelForm,Textarea,DateField,CharField
from .models import *

class RecForm(ModelForm):
    class Meta:
        model = SendRecord
        fields = ['technics','send_date','get_date','ret_date','depart','repair_reason','retus_date']
        widgets = {
            'repair_reason':Textarea(attrs={'cols':30,'rows':20})
        }

class DepartForm(ModelForm):
    class Meta:
        model = Department
        fields = ['name','short_name']

class TecForm(ModelForm):
    class Meta:
        model = Technics
        fields = ['name','t_type']
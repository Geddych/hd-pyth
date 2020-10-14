from django.forms import ModelForm,Textarea,DateField,CharField,BaseModelFormSet
from .models import *

class BaseSRFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queryset = SendRecord.objects.filter(technics__writeoff = False)


class RecForm(ModelForm):
    class Meta:
        model = SendRecord
        queryset = SendRecord.objects.filter(technics__writeoff = False)
        fields = ['technics','send_date','get_date','ret_date','repair_reason','retus_date']
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
        fields = ['name','t_type','depart']
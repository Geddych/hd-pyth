from django.forms import ModelForm,Textarea,DateField,CharField,BaseModelFormSet,PasswordInput
from .models import *
from django.contrib.auth.models import User

class RecForm(ModelForm):
    class Meta:
        model = SendRecord
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

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'password':PasswordInput()
        }
from django import forms
from app.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class DetailsForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = ['address', 'cell_no', 'is_access', 'role', 'name']


from django import forms
from .models import P

class PForm(forms.ModelForm):
    class Meta:
        model = P
        fields = '__all__'


from . models import *
from django import forms

class contact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name','email','message')
from csv import field_size_limit
from django.forms import ModelForm
from django import forms
from .models import *

class CitySearchForm(forms.ModelForm):
    class Meta:
        model = CitySearch
        fields = '__all__'
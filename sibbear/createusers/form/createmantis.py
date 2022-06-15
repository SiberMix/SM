from django import forms
from ..models import City, Position


class СreateusersForm(forms.Form):
    ticket = forms.CharField(max_length=10)
from django import forms
from cowsay.models import Cowsay



class CowsayForm(forms.Form):
    input = forms.CharField(max_length=80)
from typing import Text
from django import forms
from django.forms.widgets import TextInput

class TodoForm(forms.Form):
    content = forms.CharField( max_length=40,
    widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Enter your list here'})
    )
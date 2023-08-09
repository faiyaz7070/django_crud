from django import forms

class KeyValueForm(forms.Form):
    key = forms.CharField(label='Key', max_length=100)
    value = forms.CharField(label='Value', max_length=100)

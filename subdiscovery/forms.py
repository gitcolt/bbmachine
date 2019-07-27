from django import forms

class AddDomainForm(forms.Form):
    name = forms.CharField(label='Domain name', max_length=100)

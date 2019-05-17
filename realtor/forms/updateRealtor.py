from django.forms import ModelForm, widgets
from django import forms
from realtor.models import Realtors

class UpdateRealtor(ModelForm):
    image = forms.CharField(required=True, label='Mynd', widget=forms.TextInput(attrs={'class': 'form-control'}))

    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'email'}))
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'description'}))

    class Meta:
        model = Realtors
        exclude = ['id','name','password']
        fields = [
            'image',
            'email',
            'description'
        ]

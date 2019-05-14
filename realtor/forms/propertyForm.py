from django.forms import ModelForm, widgets
from django import forms
from property.models import Properties
from django.utils.translation import ugettext_lazy as _

class PropertyCreateForm(ModelForm):
    image = forms.CharField(required=True, label='Mynd', widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Properties
        exclude = ['id']
        widgets = {
            'streetName': widgets.TextInput(attrs={ 'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={ 'class': 'form-control'}),
            'propValue': widgets.NumberInput(attrs={ 'class': 'form-control'}),
            'fireInsurance': widgets.NumberInput(attrs={ 'class': 'form-control'}),
            'squareMeter': widgets.NumberInput(attrs={ 'class': 'form-control'}),
            'rooms': widgets.NumberInput(attrs={ 'class': 'form-control'}),
            'type': widgets.TextInput(attrs={ 'class': 'form-control'}),
            'zip': widgets.TextInput(attrs={ 'class': 'form-control'}),
            'description': widgets.Textarea(attrs={ 'class': 'form-control'}),
            'shortDescription': widgets.Textarea(attrs={ 'class': 'form-control'}),
            'realtor': widgets.Select(attrs={ 'class': 'form-control'}),
            'zone': widgets.TextInput(attrs={ 'class': 'form-control'}),
        }
        labels = {
            'streetName': _('Götuheiti'),
            'price': _('Verð'),
            'propValue': _('Fasteignamat'),
            'fireInsurance': _('Brunabótamat'),
            'squareMeter': _('Fermetrar'),
            'rooms': _('Herbergi'),
            'type': _('Tegund'),
            'zip': _('Póst númer'),
            'description': _('Lýsing'),
            'shortDescription': _('Stutt lýsing'),
            'realtor': _('Fasteignasali'),
            'zone': _('Svæði'),
        }

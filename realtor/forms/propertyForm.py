from django.forms import ModelForm, widgets
from django import forms
from property.models import Properties
from django.utils.translation import ugettext_lazy as _
from realtor.choices import *

class PropertyCreateForm(ModelForm):
    image = forms.CharField(required=True, label='Mynd', widget=forms.TextInput(attrs={'class': 'form-control'}))
    zone = forms.ChoiceField(choices=ZONE_CHOICES, required=True, label='Staður', widget=forms.Select(attrs={'class': 'form-control'}))
    zip = forms.ChoiceField(choices=ZIP_CHOICES, required=True, label='Póst númer', widget=forms.Select(attrs={'class': 'form-control'}))
    extra_field_count = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        extra_fields = kwargs.pop('extra', 0)

        super(PropertyCreateForm, self).__init__(*args, **kwargs)
        self.fields['extra_field_count'].initial = extra_fields
        for index in range(int(extra_fields)):
            # generate extra fields in the number specified via extra_fields
            self.fields['extra_field_{index}'.format(index=index)] = \
                forms.CharField()

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
            'description': widgets.Textarea(attrs={ 'class': 'form-control'}),
            'shortDescription': widgets.Textarea(attrs={ 'class': 'form-control'}),
            'realtor': widgets.Select(attrs={ 'class': 'form-control'}),
        }
        labels = {
            'streetName': _('Götuheiti'),
            'price': _('Verð'),
            'propValue': _('Fasteignamat'),
            'fireInsurance': _('Brunabótamat'),
            'squareMeter': _('Fermetrar'),
            'rooms': _('Herbergi'),
            'type': _('Tegund'),
            'description': _('Lýsing'),
            'shortDescription': _('Stutt lýsing'),
            'realtor': _('Fasteignasali'),

        }

        fields = [
            'streetName',
            'price',
            'propValue',
            'fireInsurance',
            'squareMeter',
            'rooms',
            'type',
            'zone',
            'zip',
            'description',
            'shortDescription',
            'realtor',
            'image'
        ]

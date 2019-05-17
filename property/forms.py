from django import forms
from django.forms import ModelForm, widgets
from user.models import Buyers
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField


class buyStepOneForm(ModelForm):
    class Meta:
        model = Buyers
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'ssn': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.EmailInput(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip': widgets.Select(attrs={'class': 'form-control'}),
            'country': widgets.TextInput(attrs={'class': 'form-control'})
        }



#    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control validate', 'id': 'orangeForm-pass',
#                           'placeholder': 'Vinsamlega skráðu nafn hér.'}),label='Nafn:', max_length=100, required=True)
#    ssn = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control validate', 'id': 'orangeForm-pass',
#                               'placeholder': 'Vinsamlega skráðu kennitölu hér.', 'max-lenght': 10}),label='Kennitala:', max_length=100, required=True)
#    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control validate', 'id': 'orangeForm-pass',
#                              'placeholder': 'Vinsamlega skráðu eigin netfang hér.'}),label='Netfang:', required=True)
#    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control validate', 'id': 'orangeForm-pass',
#                                  'placeholder': 'Vinsamlega skráðu heimilisfang hér.', 'max-lenght': 3}),label='Heimilisfang:', required=True)
#    zip = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control validate', 'id': 'orangeForm-pass',
#                                 'placeholder': 'Vinsamlega skráðu inn póstnúmer hér.'}), label='Póstnúmer:', required=True)
#    country = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control validate', 'id': 'orangeForm-pass',
 #                                'placeholder': 'Vinsamlega skráðu inn Land hér.'}), label='Land:', required=True)


class PaymentForm(forms.Form):
    cc_number = CardNumberField(label='Card Number')
    cc_expiry = CardExpiryField(label='Expiration Date')
    cc_code = SecurityCodeField(label='CVV/CVC')


class ReviewForm(forms.Form):
    pass
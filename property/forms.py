from django import forms
from django.forms import ModelForm, widgets


from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField


class buyStepOneForm(forms.Form):


    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control validate', 'id': 'orangeForm-pass',
                          'placeholder': 'Vinsamlega skráðu nafn hér.'}),label='Nafn:', max_length=100, required=True)
    ssn = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control validate', 'id': 'orangeForm-pass',
                              'placeholder': 'Vinsamlega skráðu kennitölu hér.', 'max-lenght': 10}),label='Kennitala:', max_length=100, required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control validate', 'id': 'orangeForm-pass',
                             'placeholder': 'Vinsamlega skráðu eigin netfang hér.'}),label='Netfang:', required=True)
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control validate', 'id': 'orangeForm-pass',
                                 'placeholder': 'Vinsamlega skráðu heimilisfang hér.', 'max-lenght': 3}),label='Heimilisfang:', required=True)
    zip = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control validate', 'id': 'orangeForm-pass',
                                'placeholder': 'Vinsamlega skráðu inn póstnúmer hér.'}), label='Póstnúmer:', required=True)
    country = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control validate', 'id': 'orangeForm-pass',
                               'placeholder': 'Vinsamlega skráðu inn Land hér.'}), label='Land:', required=True)
    def save(self):
        self.nameClean = self.cleaned_data['name']
        self.ssnClean = self.cleaned_data['ssn']
        self.emailClean = self.cleaned_data['address']
        self.zipClean = self.cleaned_data['zip']
        self.countryClean = self.cleaned_data['country']


class PaymentForm(forms.Form):
    cc_number = CardNumberField(label='Card Number', widget=forms.TextInput(attrs={'class': 'form-control validate', 'id': 'orangeForm-pass',}))
    cc_expiry = CardExpiryField(label='Expiration Date', widget=forms.TextInput(attrs={'class': 'form-control validate', 'id': 'orangeForm-pass',}))
    cc_code = SecurityCodeField(label='CVV/CVC', widget=forms.TextInput(attrs={'class': 'form-control validate', 'id': 'orangeForm-pass',}))

    def save(self):
        self.cc_numberClean = self.cleaned_data['cc_number']
        self.cc_expiryClean = self.cleaned_data['cc_expiry']
        self.cc_codeClean = self.cleaned_data['cc_code']

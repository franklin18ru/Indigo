from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control validate', 'id': 'orangeForm-pass',
                           'placeholder': 'Vinsamlega skráið nafn hér.'}),
                           max_length=100, required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control validate', 'id': 'orangeForm-pass',
                             'placeholder': 'Vinsamlega skráið eigin netfang hér.'}), required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control validate', 'id': 'orangeForm-pass',
                             'placeholder': 'Vinsamlega skráið fyrirspurn hér.'}), required=True)

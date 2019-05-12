from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




# class LoginForm(AuthenticationForm):
#     username = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'input-box'}), required=True, label='Netfang')
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'input-box'}), required=True, label='Lykilorð')
#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'password'
#         ]
#     def login(self):
#         user = super(LoginForm, self)
#         return user.clean()

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control validate', 'id': 'orangeForm-pass'}),
        required=True)
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control validate', 'id': 'orangeForm-pass'}),
        required=True)
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control validate', 'id': 'orangeForm-pass'}),
        required=True)
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control validate', 'id': 'orangeForm-pass'}),
        required=True,min_length=4)

    class Meta:
        model = User
        fields = [
            'first_name',
            'username',
            'password1',
            'password2'
        ]

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.email = user.username
        if commit:
            user.save()

        return user

    def getUser(self):
        return self.cleaned_data['username']
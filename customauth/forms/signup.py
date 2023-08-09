from django import forms
from chatroom.models import Country, State


class SignUpForm(forms.Form):
    """ Custom signup form """
    name = forms.CharField(
        label="name",
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'name',
            'placeholder': 'Name',
            'autofocus': True,
        })
    )
    username = forms.CharField(
        label="username",
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'username': 'username',
            'placeholder': 'Username',
            'autofocus': True,
        })
    )
    country = forms.ModelChoiceField(
        label='Country',
        queryset=Country.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
    state = forms.ModelChoiceField(
        label='State',
        queryset=State.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
    email = forms.CharField(
        label="Email",
        max_length=255,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'name': 'email',
            'placeholder': 'Email',
            'autofocus': True,
        })
    )
    password = forms.CharField(
        label="Password",
        max_length=30,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'name': 'password',
            'placeholder': 'Password',
        })
    )
    confirm_password = forms.CharField(
        label="Confirm Password",
        max_length=30,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'name': 'confirm_password',
            'placeholder': 'Confirm Password',
        })
    )

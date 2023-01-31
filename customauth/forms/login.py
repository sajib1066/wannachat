from django import forms


class LoginForm(forms.Form):
    """ Custom login form """
    username_or_email = forms.CharField(
        label="Email",
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'username_or_email',
            'placeholder': 'Username or Email',
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

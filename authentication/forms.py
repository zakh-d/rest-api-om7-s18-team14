from django import forms
from authentication.models import CustomUser


class CustomUserCreationForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:

        model = CustomUser
        fields = ('email', 'password', 'first_name', 'middle_name', 'last_name')


class CustomUserUpdateForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'middle_name', 'last_name')

import uuid

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = get_user_model()
        fields = "first_name", "last_name", "email", "password1", "password2",
        _placeholders = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email",
            "password1": "Password",
            "password2": "Confirm Password"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for pholder_field, pholder_text in self.Meta._placeholders.items():
            self.fields[pholder_field].widget.attrs['placeholder'] = pholder_text

    def save(self, commit=True):
        user = super().save(commit=False)
        if user.username:
            return super().save(commit)

        if user.first_name and user.last_name:
            user.username = f"{user.first_name }_{user.last_name}_{uuid.uuid4().hex}"

        if commit:
            user.save()

        return user

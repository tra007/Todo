from django import forms
from django.core import validators
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User


class loginForm(forms.Form):
    username = forms.CharField(
        widget=forms.EmailInput(attrs={"placeholder": "enter email address", "class": "FormItem"}), label="email")
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "enter password", "class": "FormItem"}),
        label="password")


class registerForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "enter email address", "class": "FormItem"}), label="email")
    name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "enter name", "class": "FormItem"}), label="name")
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "enter password", "class": "FormItem"}, ),
        validators=[
            validators.MinLengthValidator(limit_value=8,
                                          message="must be more than 8 Character")],
        label="password")
    passwordConfirm = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "enter password again", "class": "FormItem"}),
        label="password Confirm")

    def clean_passwordConfirm(self):
        password = self.cleaned_data.get("password")
        confirmPassword = self.cleaned_data.get("passwordConfirm")
        if password and confirmPassword:
            if password != confirmPassword:
                self.add_error("passwordConfirm","not equal to the password")
            return password

    def clean_email(self):
        cleanData = self.cleaned_data
        try:
            query = User.objects.get(username=cleanData["email"])
            self.add_error("email", "this email was registered")
        except ObjectDoesNotExist:
            return cleanData["email"]

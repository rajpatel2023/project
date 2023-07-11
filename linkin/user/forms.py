from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
import re
from .models import Profile


class Usersignup(UserCreationForm):
    email = forms.EmailField()

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password1")
        email_validate = re.search(r"^[\w]+@([\w-]+\.)+[\w-]{2,4}$", email)
        if email_validate is None:
            raise ValidationError("Email NOT Match Regex")
        password_validate = (
            r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@$!%*?&])(?=.*[a-zA-Z]).{8,}$",
            password,
        )
        if password_validate is None:
            raise ValidationError("password NOT Match Regex")
        return cleaned_data

    def save(self):
        userobj = super().save()
        Profile.objects.create(user=userobj)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class userprofileform(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ("user",)

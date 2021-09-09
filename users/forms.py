from django import forms
from django.db import models
from ekohms.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone=models.CharField(max_length=12)

    class Meta:
        model = User
        fields =['username','email','password1','password2','phone']
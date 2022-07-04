from django import forms
from crowdFund.models import *
from django.forms import ModelForm

class LForm(ModelForm):
    class Meta:
        model = Myuser
        fields = (
            'username',
            'password',
        )


class RForm(ModelForm):
    class Meta:
        model = Myuser
        fields = (
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'profile_pic',
            'phone_number',
        )


class EForm(ModelForm):
    class Meta:
        model = Myuser
        fields = (
            'first_name',
            'last_name',
            'profile_pic',
            'phone_number',
            'facebook_profile',
            'country',
            'Birthdate',
        )
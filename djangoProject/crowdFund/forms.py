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


class CreateProject(ModelForm):
    class Meta:
        model = projects
        fields = (
            'title',
            'category',
            'total_target',
            'start_date',
            'end_date',
            'details',
            'project_pic_main',
        )

class createImage(ModelForm):
    class Meta:
        model = imagesprject
        fields = (
            'nameproject',
            'image',
        )

class CreateTag(ModelForm):
    class Meta:
        model = TagProject
        fields = (
            'nameproject',
            'tags',
        )
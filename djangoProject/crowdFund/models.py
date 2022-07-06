from django.db import models
import datetime
import os
Categories = (
    ("one", "one"),
    ("two", "two"),
    ("three", "three"),
)

class Myuser(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=20, unique=True)
    email=models.EmailField(max_length=50,null=False)
    password=models.CharField(max_length=20)
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    Birthdate = models.DateField(null=True)
    phone_number =  models.CharField(null=True,max_length=11)
    profile_pic = models.ImageField(upload_to='profileimage', blank=False)
    country = models.CharField(max_length=20,null=True )
    facebook_profile = models.CharField(null=True,max_length=20)
    donations = models.BigIntegerField(default=0)

class projects(models.Model):
    project_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, unique=True)
    details = models.TextField(max_length=200)
    total_target = models.IntegerField()
    start_date = models.DateField()
    project_pic_main = models.ImageField(upload_to='profileimage', blank=False)
    end_date = models.DateField()
    category = models.CharField(max_length=5, choices=Categories)
    create = models.CharField(max_length=20, null=False)




class imagesprject(models.Model):
    id = models.AutoField(primary_key=True)
    nameproject = models.CharField(max_length=20)
    image = models.ImageField(upload_to='profileimage', blank=False)

class TagProject(models.Model):
    id = models.AutoField(primary_key=True)
    nameproject = models.CharField(max_length=20)
    tags = models.CharField(max_length=20)


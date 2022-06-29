from django.db import models
import datetime
import os
def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)

class Myuser(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=20)
    email=models.EmailField(max_length=50,null=False)
    password=models.CharField(max_length=20)
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    Birthdate = models.DateField(null=True)
    phone_number =  models.CharField(null=True,max_length=11)
    profile_pic = models.ImageField(upload_to='profile_pic/',null=True)
    country = models.CharField(max_length=20,null=True )
    facebook_profile = models.URLField(null=True)


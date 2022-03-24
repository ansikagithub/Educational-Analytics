from django.db import models
from django import forms

# Create your models here.
# 'ENGINE': 'django.db.backends.sqlite3',
# 'NAME': BASE_DIR / 'db.sqlite3',


class signup(models.Model):
    username=models.TextField(max_length=191)
    fname=models.TextField(max_length=191)
    lname=models.TextField(max_length=191)
    email=models.TextField(max_length=191)
    pass1=models.TextField(max_length=191)
    pass2=models.TextField(max_length=191)
        
class signin(models.Model):
    username=models.TextField(max_length=191)
    pass1=models.TextField(max_length=191)

class uploadfolder(models.Model):
    """ my application """
    File_to_upload = models.FileField(upload_to='')

class uploadfileform(forms.Form):
    title=forms.CharField(max_length=50)
    file=forms.FileField()
    

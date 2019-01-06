from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
	id_no=models.CharField(max_length=100, primary_key=True)
	name=models.CharField(max_length=150)
	college_name=models.CharField(max_length=250)
	password=models.CharField(max_length=50)
	

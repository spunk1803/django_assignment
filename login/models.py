from django.db import models

class Profile(models.Model):
	name=models.CharField(max_length=50)
	username=models.CharField(max_length=20)
	password=models.CharField(max_length=50)
	email=models.EmailField()
	gender=models.CharField(max_length=5)
	branch=models.CharField(max_length=30)
	about=models.TextField()
	profile_pic=models.ImageField(upload_to='./login/')
	cover_pic=models.ImageField(upload_to='./login/')



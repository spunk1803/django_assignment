from django import forms
from .models import Profile
#class UpdateForm(forms.ModelForm):
#	name=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'readonly':'readonly'}))
#	email=forms.EmailField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
#	password=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'readonly':'readonly'}))
#	gender=forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}))
#	class Meta:
#		model=Profile
#		fields=['branch','about','profile_pic','cover_pic']

class UpdateForm(forms.Form):
	branch=forms.CharField(max_length=50)
	about=forms.CharField()
	name=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'readonly':'readonly'}))
	email=forms.EmailField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
#	password=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'readonly':'readonly'}))
	gender=forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}))
#	profile_pic=forms.ImageField()
#	cover_pic=forms.ImageField()

class LoginForm(forms.ModelForm):
	class Meta:
		model=Profile
		fields=['username','password']
class SignupForm(forms.ModelForm):
	class Meta:
		model=Profile
		fields=('name','username','password','gender','email','branch','about',)
class PasswordForm(forms.Form):
	password=forms.CharField(widget=forms.PasswordInput())
	new_pass=forms.CharField(widget=forms.PasswordInput())
	
		

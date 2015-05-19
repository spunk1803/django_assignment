from django import forms
from .models import Profile

class LoginForm(forms.ModelForm):
	class Meta:
		model=Profile
		fields=['username','password']
class SignupForm(forms.ModelForm):
	class Meta:
		model=Profile
		fields=('name','username','password','gender','email','branch','about','profile_pic','cover_pic',)
class PasswordForm(forms.Form):
	password=forms.CharField(widget=forms.PasswordInput())
	new_pass=forms.CharField(widget=forms.PasswordInput())
	
		

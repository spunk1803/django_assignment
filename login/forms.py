from django import forms
from .models import Profile

class loginform(forms.ModelForm):
	class Meta:
		model=Profile
		fields=['username','password']
class signupform(forms.ModelForm):
	class Meta:
		model=Profile
		fields=('name','username','password','gender','email','branch','about',)
class passwordform(forms.ModelForm):
	new_pass=forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model=Profile
		fields=['password']
		

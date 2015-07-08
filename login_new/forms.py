from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
	class Meta:
		model=Profile

class LoginForm(forms.ModelForm):
	class Meta:
		model=Profile
		fields=['username','password']

class UpdateForm(forms.ModelForm):
	name=forms.CharField(max_length=30, widget=forms.TextInput(attrs={'readonly':'readonly'}))
	email=forms.EmailField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
	gender=forms.TextField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
	class Meta:
		model=Profile
		fields=['username','password','brancj','about']

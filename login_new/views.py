from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView, View
from .models import Profile
import forms

class CreateProfileView(CreateView):
	model=Profile
	template_name='signup.html' 
	form_class=form.ProfileForm
	def get_success_url(self):
		return reverse('home')

class UpdateProfileView(UpdateView):
	model=Profile
	template_name='update.html'
	form_class=form.ProfileForm
	def get_success_url(self):
		return reverse('home')

class ProfileView(DetailView):
	model=Profiel
	template_name='profile.html'

class HomeView(View):
	def post(self,request):
		

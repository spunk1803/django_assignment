from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, CreateView, UpdateView, View
from .models import Profile
import forms
from django.core.urlresolvers import reverse
 
class CreateProfileView(CreateView):
	model=Profile
	template_name='signup.html' 
	form_class=forms.ProfileForm
	def get_success_url(self):
		return reverse('home')

class UpdateProfileView(UpdateView):
	model=Profile
	template_name='update.html'
	form_class=forms.UpdateForm
	def get_success_url(self):
		return reverse('home')

class ProfileView(DetailView):
	model=Profile
	template_name='profile.html'

class LoginView(CreateView):
	model=Profile
	template_name='login.html'
	form_class=forms.LoginForm
#	def get_success_url(self):
	def post(self,request):
		form=forms.LoginForm(request.POST)
		if form.is_valid():
			data=form.cleaned_data
			user=get_object_or_404(Profile,data['username'])
			if user.password == data['password']:
				request.session['user']=user.username
				return reverse('home')
			else:
				return reverse('login')
		else:
			return reverse('login')		

class LogoutView(View):
	model=Profile
	template_name='logout.html'
	def get_success_url(self,request):
		del request.session['user']
		return reverse('home')

class HomeView(View):
	model=Profile
	template_name='home.html'
	def get_success_url(self):
		return reverse('home')
	def get_context_data(self, **kwargs):
		context=super(HomeView,self).get_context_data(**kwargs)
		if request.session['user']:
			context['status']=True
		else:
			context['status']=False
		return context
		

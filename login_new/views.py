from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, CreateView, UpdateView, TemplateView, View
from .models import Profile
import forms
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
class CreateProfileView(CreateView):
	model=Profile
	template_name='signup.html' 
	def get_success_url(self):
		user=User.objects.create_user(username=self['username'],password=self['password'])
		user.save()
		return reverse('home')
class LoginView(View):
#	model=Profile
	template_name='login.html'
	form_class=forms.LoginForm
#	form_class=forms.LoginForm
#	def get_success_url(self):
	def post(self,request, *args, **kwargs):
		form=self.form_class(request.POST)
		if form.is_valid():
			data=form.cleaned_data
			user=authenticate(username=data['username'],password=data['password'])
			if user is not None:
				login(request,user)

class HomeView(TemplateView):
#	model=Profile
	template_name='home.html'
#	def get_success_url(self):
#		return reverse('home')
	def get_context_data(self, **kwargs):
		context=super(HomeView,self).get_context_data(**kwargs)
		if request.user.is_authenticated():
			context['status']=True
			context['user']=request.user
		else:
			context['status']=False
		return context
	
@login_required
class UpdateProfileView(UpdateView):
	model=Profile
	template_name='update.html'
	form_class=forms.UpdateForm
	def get_success_url(self):
		return reverse('home')
@login_required
class ProfileView(DetailView):
	model=Profile
	template_name='profile.html'

@login_required
#class LogoutView(TemplateView):
#	model=Profile
#	template_name='logout.html'
#	def logout_func(request):	
#		logout(request)
#		return reverse('home')
#	logout_func(request)
#	def get_success_url(self):
#		return reverse('home')
def LogoutView(request):
	logout(request)
	return reverse('home')
	

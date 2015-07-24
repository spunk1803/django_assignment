from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, CreateView, UpdateView, TemplateView, View
from .models import Profile
import forms
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.utils.decorators import method_decorator
class CreateProfileView(CreateView):
	model=Profile
	template_name='signup.html' 
	form_class=forms.SignupForm
	def post(self,request, *args, **kwargs):
		form=self.form_class(request.POST)
		if form.is_valid():
			data=form.cleaned_data
			user=User.objects.create_user(username=data['username'],email=data['email'],password=data['password'])
			user=form.save()
			user.save()
			
			return redirect('home')
		return render(request, self.template_name, {'form':form})
	def get(self, request, *args, **kwargs):
		form=self.form_class()
		return render(request, self.template_name, {'form':form})

def LoginView(request):
	if request.method=="POST":
		form=forms.LoginForm(request.POST)
		if form.is_valid():
			data=form.cleaned_data
			user=authenticate(username=data['username'], password=data['username'])
			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				return redirect('login')
	else:
		form=forms.LoginForm()
	return render(request, 'login.html', {'form':form})
def HomeView(request):
	if request.user.is_authenticated() :
		user=get_object_or_404(Profile, username=request.user.username)
	else:
		user=None
	return render(request, 'home.html', {'user':user})	
	
#@login_required
class UpdateProfileView(UpdateView):
	model=Profile
	template_name='update.html'
	form_class=forms.UpdateForm
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
        	return super(UpdateProfileView, self).dispatch(*args, **kwargs)	
	def get_success_url(self):
		return reverse('home')
#@login_required
class ProfileView(DetailView):
	model=Profile
	template_name='profile.html'
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
        	return super(ProfileView, self).dispatch(*args, **kwargs)	
@login_required
def LogoutView(request):
	logout(request)
	return redirect('home')
	

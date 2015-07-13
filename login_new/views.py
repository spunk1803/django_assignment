from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, CreateView, UpdateView, TemplateView, View
from .models import Profile
import forms
from django.core.urlresolvers import reverse
 
class CreateProfileView(CreateView):
	model=Profile
	template_name='signup.html' 
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
			user=get_object_or_404(Profile,data['username'])
			if user.password == data['password']:
				request.session['user']=user.username
				return redirect('home')
			else:
				return redirect('login')
		return render(request, self.template_name, {'form': form})

class LogoutView(TemplateView):
#	model=Profile
	template_name='logout.html'
	def get_success_url(self,request):
		del request.session['user']
		return reverse('home')

class HomeView(TemplateView):
#	model=Profile
	template_name='home.html'
#	def get_success_url(self):
#		return reverse('home')
	def get_context_data(self, **kwargs):
		context=super(HomeView,self).get_context_data(**kwargs)
		if request.session['user']:
			context['status']=True
		else:
			context['status']=False
		return context
		

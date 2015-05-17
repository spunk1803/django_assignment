from django.shortcuts import render,redirect,get_object_or_404
from .models import Profile
from .forms import signupform,loginform,passwordform
#from django.core.urlresolvers import reverse
#from django.http import HttpResponseRedirect

def login(request):
	if request.method=="POST":
		form=loginform(request.POST)
		if form.is_valid() :
			data=form.cleaned_data
			details=get_object_or_404(Profile, username=data['username'])
			return redirect('home', pk=details.pk)

	else:
		form=loginform()
	return render(request, 'login/login.html',{'form': form})
def home(request, pk=None):
	if pk:
		user=get_object_or_404(Profile,pk=pk)
	else:
		user=Profile()
	return render(request, 'login/home.html', {'user':user})
	
def signup(request):
	if request.method=="POST":
		form=signupform(request.POST)
		if form.is_valid():
			profile=form.save()
			profile.save()
			return redirect('login.views.home', pk=profile.pk)
	else:
		form=signupform()
	return render(request, 'login/signup.html',{'form':form} )
def profile(request,pk=None):
	if pk:
		details=get_object_or_404(Profile,pk=pk)
		return render(request, 'login/profile.html', {'details':details})
	else:
		return redirect('login.views.login')
def changepass(request,pk=None):
	if pk:
		user=get_object_or_404(Profile,pk=pk)
		if request.method=="POST":
			form=passwordform(request.POST)
			user.password=form.cleaned_data['new_pass']
			user.save()
			return redirect('home', pk=user.pk)
		else:
			form=passwordform()
			return render(request, 'login/change_password.html', {'form':form})
	else:
		return redirect('login.views.home')
		

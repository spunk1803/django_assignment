from django.shortcuts import render,redirect,get_object_or_404
from .models import Profile
from .forms import SignupForm,LoginForm,PasswordForm
from django.contrib.auth import login,authenticate
def login(request):
	if request.method=="POST":
		form=LoginForm(request.POST)
		if form.is_valid() :
			data=form.cleaned_data
			user=authenticate(username=data['username'],password=data['password'])
			if user is not None:
				login(request,user)
				return redirect('home')
			else:
				return redirect('login')
	else:
		form=LoginForm()
	return render(request, 'login/login.html',{'form': form})

#def login(request):
#	if request.method=="POST":
#		form=LoginForm(request.POST)
#		if form.is_valid() :
#			data=form.cleaned_data
#			details=get_object_or_404(Profile, username=data['username'])
#			if details.password == data['password']:
#				return redirect('home', pk=details.pk)
#			else:
#				return redirect('login')
#	else:
#		form=LoginForm()
#	return render(request, 'login/login.html',{'form': form})
def home(request):
	return render(request, 'login/home.html', {'user': request.user})
#def home(request, pk=None):
#	if pk:
#		user=get_object_or_404(Profile,pk=pk)
#	else:
#		user=Profile()
#	return render(request, 'login/home.html', {'user':user})	
def signout(request):
	logout(request)
	return redirect('home')
def signup(request):
	if request.method=="POST":
		form=SignupForm(request.POST,request.FILES)
		if form.is_valid():
			profile=form.save()
			profile.save()
			user=authenticate(username=profile.username,password=profile.password)
			login(request,user)
			return redirect('login.views.home')
	else:
		form=SignupForm()
	return render(request, 'login/signup.html',{'form':form} )

#def signup(request):
#	if request.method=="POST":
#		form=SignupForm(request.POST,request.FILES)
#		if form.is_valid():
#			profile=form.save()
#			profile.save()
#			return redirect('login.views.home', pk=profile.pk)
#	else:
#		form=SignupForm()
#	return render(request, 'login/signup.html',{'form':form} )
def profile(request):
	if request.user.is_aunthenticated():
		return render(request, 'login/profile.html',{'user':request.iuser})
	else:
		return redirect('login.views.login')
#def profile(request,pk=None):
#	if pk:
#		details=get_object_or_404(Profile,pk=pk)
#		return render(request, 'login/profile.html', {'details':details})
#	else:
#		return redirect('login.views.login')
#def changepass(request,pk=None):
#	if pk:
#		user=get_object_or_404(Profile,pk=pk)
#		if request.method=="POST":
#			form=PasswordForm(request.POST)
#			if form.is_valid():
#				if user.password==form.cleaned_data['password']:
#					user.password=form.cleaned_data['new_pass']
#					user.save()
#					return redirect('home', pk=user.pk)
#				else:
#					return redirect('changepass',pk=user.pk)
#			else:
#				return redirect('changepass',pk=user.pk)
#		else:
#			form=PasswordForm()
#			return render(request, 'login/change_password.html', {'form':form})
#	else:
#		return redirect('login.views.home')
def changepass(request):
	if request.user.is_aunthenticated():
		if request.method=='POST':
			form=PasswordChangeForm(user=request.user, data=request.POST)
			if form.is_valid():
				form.save()
				update_session_auth_hash(request, form.user)
				return redirect('home')
				
			else:
				return redirect('changepass')
		else:
			form=PasswordForm()
			return render(request, 'login/change_password.html', {'form':form})
	
						
	else:
		return redirect('login.views.home')

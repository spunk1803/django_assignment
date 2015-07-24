from django.shortcuts import render,redirect,get_object_or_404
from .models import Profile
from .forms import SignupForm,LoginForm,PasswordForm, UpdateForm
def login(request):
	if request.method=="POST":
		form=LoginForm(request.POST)
		if form.is_valid() :
			data=form.cleaned_data
			user=get_object_or_404(Profile, username=data['username'])
			if user.password == data['password']:
				request.session['username']=user.username
				return redirect('home')
			else:
				return redirect('login')
	else:
		form=LoginForm()
	return render(request, 'login/login.html',{'form': form})
def home(request):
	return render(request, 'login/home.html', {})	
def signout(request):
	del request.session['username']
	return redirect('home')
def signup(request):
	if request.method=="POST":
		form=SignupForm(request.POST,request.FILES)
		if form.is_valid():
			profile=form.save()
			profile.save()
			return redirect('login.views.home')
	else:
		form=SignupForm()
	return render(request, 'login/signup.html',{'form':form} )
def profile(request):
	if request.session['username']:
		user=get_object_or_404(Profile,username=request.session['username'])
		return render(request, 'login/profile.html', {'user': user})
	else:
		return redirect('login.views.login')
def update(request):
	user=get_object_or_404(Profile,username=request.session['username'])
	if request.method=='POST':
		form=UpdateForm(request.POST)
		if form.is_valid():
			data=form.cleaned_data
			user.branch=data['branch']
			user.about=data['about']
#			user.profile_pic=data['profile_pic']
#			user.cover_pic=data['cover_pic']
			user.save()
			return redirect('home')
		else:
			return redirect('update')
	else:
		form=UpdateForm(user.__dict__)
	return render(request, 'login/update.html', {'form':form})
def changepass(request):
	if request.session['username']:
		user=get_object_or_404(Profile,username=request.session['username'])
		if request.method=="POST":
			form=PasswordForm(request.POST)
			if form.is_valid():
				if user.password==form.cleaned_data['password']:
					user.password=form.cleaned_data['new_pass']
					user.save()
					return redirect('home')
				else:
					return redirect('changepass')
			else:
				return redirect('changepass')
		else:
			form=PasswordForm()
			return render(request, 'login/change_password.html', {'form':form})
	else:
		return redirect('login.views.home')


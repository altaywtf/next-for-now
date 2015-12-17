from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import C_Owner
from .forms import COwnerCreationForm, ApplicantCreationForm, LoginForm

REDIRECT_PAGE = '/user/signup/cowner/'

def cOwnerSignUpView(request):
	if request.method == 'POST':
		form = COwnerCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(REDIRECT_PAGE)
	else:
		form = COwnerCreationForm()
	return render(request, 'user/userform.html', {'form':form})

def applicantSignUpView(request):
	if request.method == 'POST':
		form = ApplicantCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(REDIRECT_PAGE)
	else:
		form = ApplicantCreationForm()
	return render(request, 'user/userform.html', {'form':form})

def loginView(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(username=request.POST['username'],password=request.POST['password'])
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(REDIRECT_PAGE)
			else:
				return HttpResponseRedirect(REDIRECT_PAGE)
		else:
			return HttpResponseRedirect(REDIRECT_PAGE)
	else:
		form = LoginForm()
	return render(request, 'user/userform.html', {'form':form})

def logoutView(request):
	logout(request)
	return HttpResponseRedirect(REDIRECT_PAGE)

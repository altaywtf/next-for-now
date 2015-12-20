from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import C_Owner
from .forms import COwnerCreationForm, ApplicantCreationForm, LoginForm

REDIRECT_PAGE = '/user/signup/cowner/'
REDIRECT_LOGIN = '/user/login'

def cOwnerSignUpView(request):
	if request.method == 'POST':
		form = COwnerCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(REDIRECT_LOGIN)
	else:
		if request.user.is_authenticated():
			return HttpResponseRedirect('/')
		form = COwnerCreationForm()
	return render(request, 'user/userform.html', {'form':form})

def applicantSignUpView(request):
	if request.method == 'POST':
		form = ApplicantCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(REDIRECT_LOGIN)
	else:
		if request.user.is_authenticated():
			return HttpResponseRedirect('/')
		form = ApplicantCreationForm()
	return render(request, 'user/userform.html', {'form':form})

def loginView(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(username=request.POST['username'],password=request.POST['password'])
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(request.GET["next"])
			else:
				return HttpResponseRedirect(request.GET["next"])
		else:
			return render_to_response('user/userform.html', {'form':form}, context_instance=RequestContext(request))
	else:
		if request.user.is_authenticated():
			return HttpResponseRedirect('/')
		form = LoginForm()
	return render_to_response('user/userform.html', {'form':form}, context_instance=RequestContext(request))

def logoutView(request):
	logout(request)
	return HttpResponseRedirect('/')

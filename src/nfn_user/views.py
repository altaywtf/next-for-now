from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import C_Owner
from .forms import COwnerCreationForm, ApplicantCreationForm

REDIRECT_PAGE = '/user/signup/cowner/'

def cOwnerSignUpView(request):
	if request.method == 'POST':
		form = COwnerCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(REDIRECT_PAGE)
	else:
		form = COwnerCreationForm()
	return render(request, 'user/signup.html', {'form':form})

def applicantSignUpView(request):
	if request.method == 'POST':
		form = ApplicantCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(REDIRECT_PAGE)
	else:
		form = ApplicantCreationForm()
	return render(request, 'user/signup.html', {'form':form})

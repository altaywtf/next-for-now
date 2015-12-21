from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import C_Owner
from .forms import COwnerCreationForm, ApplicantCreationForm, LoginForm, COwnerChangeForm, ApplicantChangeForm, ContactForm

REDIRECT_PAGE = '/user/signup/cowner/'
REDIRECT_LOGIN = '/user/login'

def SignUpView(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	return render(request, 'user/signup.html')

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
				if request.GET:
					return HttpResponseRedirect(request.GET["next"])
				else:
					return HttpResponseRedirect('/')
			else:
				return HttpResponseRedirect(request.GET["next"])
		else:
			return render_to_response('user/login.html', {'form':form}, context_instance=RequestContext(request))
	else:
		if request.user.is_authenticated():
			return HttpResponseRedirect('/')
		form = LoginForm()
	return render_to_response('user/login.html', {'form':form}, context_instance=RequestContext(request))

def logoutView(request):
	logout(request)
	return HttpResponseRedirect('/')

def userChangeView(request):
	if request.method == 'POST':
		if request.user.groups.filter(name='Contest Owner').exists():
			form = COwnerChangeForm(request.POST, instance=request.user)
		else:
			form = ApplicantChangeForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save(user=request.user)
	else:
		if request.user.groups.filter(name='Contest Owner').exists():
			cowner = C_Owner.objects.get(profile_model_referance__exact = request.user.id)
			form = COwnerChangeForm(initial={'website':cowner.website,'company_name':cowner.company_name,
				'company_address':cowner.company_address},instance=request.user)
		else:
			form = ApplicantChangeForm(instance=request.user)
	return render(request, 'user/userform_edit.html', {'form':form})

def contactView(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			recipient_list = []
			for user in User.objects.all():
				if user.is_superuser:
					recipient_list.append(user.email)
			send_mail(form.cleaned_data['subject'], form.cleaned_data['text'], 'admin@nextfornow.com',
				recipient_list)
			return HttpResponseRedirect('/')
	else:
		form = ContactForm()
	return render(request, 'user/contactform.html', {'form':form})


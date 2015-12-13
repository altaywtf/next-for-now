from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import C_Owner
from .forms import COwnerCreationForm

def cOwnerSignUpView(request):
	if request.method == 'POST':
		form = COwnerCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/user/signup/cowner/')
	else:
		form = COwnerCreationForm()
	return render(request, 'user/cownersignup.html', {'form':form})


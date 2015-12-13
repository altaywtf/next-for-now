from django.shortcuts import render
from .models import C_Owner, UserModelForm
from django.contrib.auth.models import User
from django.forms import inlineformset_factory

def cOwnerSignUpView(request):
	userForm = UserModelForm()
	user = User()
	COwnerFormSet = inlineformset_factory(User, C_Owner, can_delete=False)
	if request.method == 'POST':
		user = COwnerFormSet(request.Post)
		created_user = user.save()
		formset = COwnerFormSet(request.POST, instance=created_user)
	else:
		formset = COwnerFormSet(instance=user)
	return render(request, 'cownersignup.html', {'formset':formset})

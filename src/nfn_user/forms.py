from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import C_Owner

class COwnerCreationForm(UserCreationForm):
	website = forms.CharField(label='Website', max_length=200,)
	company_name = forms.CharField(label='Company Name', max_length=200,)
	company_address = forms.CharField(label='Company Address',widget=forms.Textarea)

	class Meta:
		model = User
		fields=("username","email")

	def save(self, commit=True):
		if not commit:
			raise NotImplementedError("Database Save Error")
		user = super(COwnerCreationForm, self).save(commit=True)
		c_owner = C_Owner(profile_model_referance=user, website=self.cleaned_data['website'], 
			company_name=self.cleaned_data['company_name'], company_address=self.cleaned_data['company_address'])
		c_owner.save()
		return user, c_owner
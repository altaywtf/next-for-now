from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm, forms
from .models import C_Owner

C_OWNER_GROUP = 'Contest Owner'
APPLICANT_GROUP = 'Applicant'

class COwnerCreationForm(UserCreationForm):
	website = forms.CharField(label='Website', max_length=200)
	company_name = forms.CharField(label='Company Name', max_length=200,)
	company_address = forms.CharField(label='Company Address', widget=forms.Textarea(attrs={'rows': 3}))

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
		Group.objects.get(name=C_OWNER_GROUP).user_set.add(user)
		return user, c_owner

class ApplicantCreationForm(UserCreationForm):
	class Meta:
		model = User
		fields=("username","email")

	def save(self, commit=True):
		if not commit:
			raise NotImplementedError("Database Save Error")
		user = super(ApplicantCreationForm, self).save(commit=True)
		Group.objects.get(name=APPLICANT_GROUP).user_set.add(user)
		return user

class COwnerChangeForm(forms.ModelForm):
	website = forms.CharField(label='Website', max_length=200)
	company_name = forms.CharField(label='Company Name', max_length=200,)
	company_address = forms.CharField(label='Company Address', widget=forms.Textarea(attrs={'rows': 3}))

	class Meta:
		model = User
		fields= {"username","email"}

	def save(self,user,commit=True):
		if not commit:
			raise NotImplementedError("Database Save Error")
		user.username = self.cleaned_data['username']
		user.email = self.cleaned_data['email']
		cowner = C_Owner.objects.get(profile_model_referance__exact = user.id)
		cowner.website = self.cleaned_data['website']
		cowner.company_name = self.cleaned_data['company_name']
		cowner.company_address = self.cleaned_data['company_address']
		user.save()
		cowner.save()

class ApplicantChangeForm(forms.ModelForm):
	class Meta:
		model = User
		fields = {"username","email"}

	def save(self,user,commit=True):
		if not commit:
			raise NotImplementedError("Database Save Error")
		user.username = self.cleaned_data['username']
		user.email = self.cleaned_data['email']
		user.save()
		

class LoginForm(forms.Form):
	username = forms.CharField(label='Username')
	password = forms.CharField(label='Password', widget=forms.PasswordInput)
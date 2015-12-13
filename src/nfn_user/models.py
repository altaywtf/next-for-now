from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


class C_Owner(models.Model):
	profile_model_referance = models.OneToOneField(User,on_delete=models.CASCADE)
	website = models.URLField('Website', max_length=200,)
	company_name = models.CharField('Company Name', max_length=200)
	company_address = models.TextField('Company Address')


class UserModelForm(ModelForm):
	class Meta:
		model = User
		fields = ['username','password','first_name','last_name','email']
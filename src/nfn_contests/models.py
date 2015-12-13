from __future__ import unicode_literals

from django.db import models
from nfn_user.models import C_Owner

class Contest(models.Model):
	Design = 'DES'
	Development = 'DEV'
	Business = 'BUS'
	Engineering = 'ENG'
	MediaProduction = 'MED'
	CreativeWriting = 'CRE'

	category_choices = (
		(Design, 'Design'),
		(Development, 'Development'),
		(Business, 'Business'),
		(Engineering, 'Engineering'),
		(MediaProduction, 'Media Production'),
		(CreativeWriting, 'Creative Writing'),
	)

	owner = models.ForeignKey(C_Owner)
	title = models.CharField('Contest Title', max_length=20)
	category = models.CharField('Contest Category', choices=category_choices, max_length=20)
	description = models.CharField('Contest Description', max_length=50)
	details = models.TextField('Contest Details')
	image = models.ImageField(upload_to='uploads/contest_img/')
	award = models.CharField('Contest Award', max_length=50)
	is_approved = models.BooleanField('Approved')
	is_ongoing = models.BooleanField('Ongoing')
	date_started = models.DateField('Contest Start Date', blank=False, null=False) 
	date_deadline = models.DateField('Contest Deadline', blank=False, null=False)
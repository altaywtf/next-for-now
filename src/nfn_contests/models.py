from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone

from nfn_user.models import C_Owner

class Contest(models.Model):
	
	category_choices = (
		('Design', 'Design'),
		('Development', 'Development'),
		('Business', 'Business'),
		('Engineering', 'Engineering'),
		('MediaProduction', 'Media Production'),
		('CreativeWriting', 'Creative Writing'),
	)

	owner = models.CharField('Contest Owner', max_length=20)
	title = models.CharField('Contest Title', max_length=20)
	category = models.CharField('Contest Category', choices=category_choices, max_length=20)
	description = models.CharField('Contest Description', max_length=50)
	details = models.TextField('Contest Details')
	image = models.ImageField(upload_to='uploads/contest_img/')
	award = models.CharField('Contest Award', max_length=50)
	''' submissions '''
	date_started = models.DateField('Contest Start Date', blank=False, null=False) 
	date_deadline = models.DateField('Contest Deadline', blank=False, null=False)

	is_approved = models.CharField('Contest Approval', choices=(('Approved', 'Approved'), ('Not Approved', 'Not Approved')), max_length=10)
	is_ongoing = models.CharField('Contest Status', choices=(('Ongoing', 'Ongoing'), ('Finished', 'Finished')), max_length=10)

	@property
	def ongoing_check(self):
		if self.date_deadline > self.date_started:
			return "Ongoing"
		return "Finished"

	def __unicode__(self):
		return self.title
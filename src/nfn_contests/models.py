from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField

from nfn_user.models import C_Owner
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField('Name', max_length=30)
	slug = AutoSlugField(populate_from='name')
	description = models.CharField('Description', max_length=100)
	hex_code = models.CharField('Color Code', max_length=7)

	def __unicode__(self):
		return self.name

class Contest(models.Model):
	owner = models.ForeignKey(C_Owner, on_delete=models.CASCADE)
	title = models.CharField(max_length=30)
	slug = AutoSlugField(populate_from='title', unique_with=['owner__company_name'])
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	description = models.CharField(max_length=50)
	details = models.TextField()
	image = models.ImageField(upload_to='../media/contests/', null=True, blank=True)
	award = models.CharField(max_length=50)
	date_started = models.DateField('Start Date', blank=False, null=False) 
	date_deadline = models.DateField('Deadline', blank=False, null=False)
	is_approved = models.BooleanField('Approved', default=True)

	@property
	def is_ongoing(self):
		if self.date_deadline > datetime.date.today():
			return "Ongoing"
		return "Finished"

	def __unicode__(self):
		return self.title


class Submission(models.Model):
	applicant = models.ForeignKey(User, on_delete=models.CASCADE)
	contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
	a_names = models.CharField('Applicant Name(s)', max_length=200)
	a_details = models.TextField('Applicant Details')
	s_details = models.TextField('Submission Details')
	s_file = models.FileField('Submission File', upload_to='../media/submissions/', null=True, blank=True)
	feedback = models.TextField('Contest Owner\'s Feedback', blank=True, null=True)
	is_winner = models.BooleanField('Winner!', default=False)
	date_posted = models.DateTimeField('Submission Date', auto_now_add=True)

	def __unicode__(self):
		return '%s %s' % (self.contest, self.applicant)

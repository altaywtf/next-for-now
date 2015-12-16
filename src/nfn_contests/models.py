from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone

from nfn_user.models import C_Owner

class Contest(models.Model):
	category_choices = (
		('design', 'Design'),
		('development', 'Development'),
		('business', 'Business'),
		('engineering', 'Engineering'),
		('mediaproduction', 'Media Production'),
		('creativewriting', 'Creative Writing'),
	)
	owner = models.ForeignKey(C_Owner, on_delete=models.CASCADE)
	title = models.CharField(max_length=30)
	category = models.CharField(choices=category_choices, max_length=30)
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

	@property
	def get_categories(self):
		categories = []
		for category in self.category_choices: categories.append(str(category[0]))
		return categories

	def __unicode__(self):
		return self.title

class Submission(models.Model):
	applicant = models.CharField('Applicant Account', max_length=20)
	contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
	a_names = models.CharField('Applicant Name(s)', max_length=200)
	a_details = models.TextField('Applicant Details')
	s_details = models.TextField('Submission Details')
	s_file = models.FileField('Submission File', upload_to='../media/submissions/', null=True)
	feedback = models.TextField('Contest Owner\'s Feedback', blank=True, null=True)
	is_winner = models.BooleanField('Winner!', default=False)
	date_posted = models.DateTimeField('Submission Date', auto_now_add=True)

	def __unicode__(self):
		return '%s %s' % (self.contest, self.applicant)

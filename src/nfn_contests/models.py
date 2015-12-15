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
	owner = models.ForeignKey(C_Owner)
	title = models.CharField(max_length=20)
	category = models.CharField(choices=category_choices, max_length=20)
	description = models.CharField(max_length=50)
	details = models.TextField()
	image = models.ImageField(upload_to='../media/contests/', blank=True, null=True)
	award = models.CharField(max_length=50)
	date_started = models.DateField('Start Date', blank=False, null=False) 
	date_deadline = models.DateField('Deadline', blank=False, null=False)
	is_approved = models.CharField('Approval', choices=(('Approved', 'Approved'), ('Not Approved', 'Not Approved')), max_length=10, blank=False, null=False)
	is_ongoing = models.CharField('Status', choices=(('Ongoing', 'Ongoing'), ('Finished', 'Finished')), max_length=10, blank=False, null=False)

	@property
	def ongoing_check(self):
		if self.date_deadline > self.date_started:
			return "Ongoing"
		return "Finished"

	def __unicode__(self):
		return self.title

class Submission(models.Model):
	applicant = models.CharField('Applicant Account', max_length=20)
	contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
	a_names = models.CharField('Applicant Name(s)', max_length=200)
	a_details = models.TextField('Applicant Details')
	s_details = models.TextField('Submission Details')
	s_file = models.FileField('Submission File', upload_to='../media/submissions/', blank=True, null=True)
	feedback = models.TextField('Contest Owner\'s Feedback', blank=True, null=True)
	is_winner = models.BooleanField('Winner!', default=False)
	date_posted = models.DateTimeField('Submission Date', auto_now_add=True)

	def __unicode__(self):
		return '%s %s' % (self.contest, self.applicant)

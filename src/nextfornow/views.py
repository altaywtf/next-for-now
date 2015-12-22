#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.views import generic
from nfn_contests.models import Category, Contest, Submission

# HomePage - Featured Contests
class IndexView(generic.ListView):
	template_name = 'index.html'
	context_object_name = 'contest_list'
	allow_empty = True

	def get_allow_empty(self):
		return self.allow_empty

	def get_queryset(self):
		return Contest.objects.filter(is_approved=True).order_by('-date_started')

# AboutPage
class AboutView(generic.TemplateView):
	template_name = 'other/about.html'
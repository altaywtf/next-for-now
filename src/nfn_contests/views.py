from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic

from .models import Contest

class IndexView(generic.ListView):
	template_name = 'contests/index.html'
	context_object_name = 'ongoing_contests_list'

	def get_queryset(self):
		return Contest.objects.all()[:5]
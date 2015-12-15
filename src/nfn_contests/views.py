from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic

from .models import Contest, Submission

class IndexView(generic.ListView):
	template_name = 'contests/index.html'
	context_object_name = 'ongoing_contests_list'

	def get_queryset(self):
		return Contest.objects.filter(is_ongoing='Ongoing')[:5]

class DetailView(generic.DetailView):
	model = Contest
	template_name = 'contests/details.html'

''' class CreateView(): '''

''' class EditView(): '''

''' class ApplyView(): '''

''' class SubmissionsView(): '''

''' class ViewSubmissionView(): '''

#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from .models import Category, Contest, Submission, Winner
from nfn_user.models import C_Owner

from .forms import ContestForm, SubmissionForm, FeedbackForm, WinnerForm

####################################################################################
# Contest Listing

# Contest Listing: List All
class IndexView(generic.ListView):
	template_name = 'contests/index.html'
	context_object_name = 'contest_list'
	allow_empty = True
	paginate_by = 4

	def get_allow_empty(self):
		return self.allow_empty

	def get_queryset(self):
		return Contest.objects.filter(is_approved=True).order_by('-date_started')

	def get_context_data(self, *args, **kwargs):
		context = super(IndexView, self).get_context_data(*args, **kwargs)
		context['contest_category_list'] = Category.objects.all()
		context['contest_owner_list'] = C_Owner.objects.all()
		return context

# Contest Listing: List Ongoing Contests
class FilterByOngoing(generic.ListView):
	template_name = 'contests/index.html'
	context_object_name = 'contest_list'
	paginate_by = 8

	# ¯\_(ツ)_/¯
	def get_queryset(self):
		q = Contest.objects.filter(is_approved=True).order_by('-date_started')
		context = []
		for contest in q:
			if contest.is_ongoing == "Ongoing":
				context.append(contest)
		return context

	def get_context_data(self, *args, **kwargs):
		context = super(FilterByOngoing, self).get_context_data(*args, **kwargs)
		context['contest_category_list'] = Category.objects.all()
		context['contest_owner_list'] = C_Owner.objects.all()
		return context

# Contest Listing: List Finished Contests
class FilterByFinished(generic.ListView):
	template_name = 'contests/index.html'
	context_object_name = 'contest_list'
	paginate_by = 8

	# ¯\_(ツ)_/¯
	def get_queryset(self):
		q = Contest.objects.filter(is_approved=True).order_by('-date_started')
		context = []
		for contest in q:
			if contest.is_ongoing == "Finished":
				context.append(contest)
		return context

	def get_context_data(self, *args, **kwargs):
		context = super(FilterByFinished, self).get_context_data(*args, **kwargs)
		context['contest_category_list'] = Category.objects.all()
		context['contest_owner_list'] = C_Owner.objects.all()
		return context

# Contest Listing: Filter by Category
class FilterByCategory(generic.ListView):
	template_name = 'contests/index_by_category.html'
	context_object_name = 'contest_list'
	paginate_by = 8

	def get_queryset(self):
		self.category = get_object_or_404(Category, slug=self.kwargs['category_slug'])
		return Contest.objects.filter(category__slug=self.kwargs['category_slug'], is_approved=True).order_by('-date_started')

	def get_context_data(self, *args, **kwargs):
		context = super(FilterByCategory, self).get_context_data(*args, **kwargs)
		context['contest_category_list'] = Category.objects.all()
		context['contest_owner_list'] = C_Owner.objects.all()
		context['category'] = Category.objects.filter(slug=self.kwargs['category_slug'])
		return context

# Contest Listing: Filter by Contest Owner
class FilterByOwner(generic.ListView):
	template_name = 'contests/index_by_company.html'
	context_object_name = 'contest_list'
	paginate_by = 8

	def get_queryset(self):
		self.owner = get_object_or_404(C_Owner, pk=self.kwargs['company_pk'])
		return Contest.objects.filter(owner_id=self.kwargs['company_pk'], is_approved=True).order_by('-date_started')

	def get_context_data(self, *args, **kwargs):
		context = super(FilterByOwner, self).get_context_data(*args, **kwargs)
		context['contest_category_list'] = Category.objects.all()
		context['contest_owner_list'] = C_Owner.objects.all()
		context['company'] = C_Owner.objects.filter(pk=self.kwargs['company_pk'])
		return context

# Contest Listing: Search Resulsts
class FilterBySearch(generic.ListView):
	template_name = 'contests/index_by_search.html'
	context_object_name = 'contest_list'
	paginate_by = 8

	def get_queryset(self):
		if self.request:
			q = self.request.GET['q']
			return Contest.objects.filter(Q(title__icontains=q) | Q(description__icontains=q) | Q(details__icontains=q)) 
		else:
			return Contest.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(FilterBySearch, self).get_context_data(*args, **kwargs)
		context['contest_category_list'] = Category.objects.all()
		context['contest_owner_list'] = C_Owner.objects.all()
		return context

####################################################################################
# Contest CRUD

# Contest Creation -accessible only for c_owner accounts-
class ContestCreate(LoginRequiredMixin, generic.CreateView):
	login_url = '/user/login/'
	form_class = ContestForm
	model = Contest
	template_name = 'contests/_form_contest.html'

	def dispatch(self, request, *args, **kwargs):
		if not self.request.user.groups.filter(name="Contest Owner"):
			raise Http404
		return super(ContestCreate, self).dispatch(request, *args, **kwargs)

	def form_valid(self, form):
		form.instance.owner = self.request.user.c_owner
		return super(ContestCreate, self).form_valid(form)

# Contest Detail View
class ContestDetail(generic.DetailView):
	model = Contest
	template_name = 'contests/details_contest.html'
	slug_field = 'slug'

	def get_context_data(self, *args, **kwargs):
		context = super(ContestDetail, self).get_context_data(*args, **kwargs)
		context['submissions'] = Submission.objects.filter(contest__slug=self.kwargs['slug'])
		if self.request.user.is_authenticated():
			context['request_user_posted'] = Submission.objects.filter(applicant=self.request.user)
		return context

# Contest Update -accesible only for contest owner-
class ContestUpdate(LoginRequiredMixin, generic.UpdateView):
	login_url = '/user/login/'
	form_class = ContestForm
	model = Contest
	template_name = 'contests/_form_contest.html'

	def get_object(self, *args, **kwargs):
		obj = super(ContestUpdate, self).get_object(*args, **kwargs)
		if not obj.owner == self.request.user.c_owner:
			raise Http404
		return obj

	def form_valid(self, form):
		form.instance.owner = self.request.user.c_owner
		return super(ContestUpdate, self).form_valid(form)

# Contest Delete -accesible only for contest owner-
class ContestDelete(LoginRequiredMixin, generic.DeleteView):
	login_url = '/user/login/'
	model = Contest
	template_name = 'contests/_form_contest_delete.html'
	success_url = reverse_lazy('contests:index')

	def get_object(self, *args, **kwargs):
		obj = super(ContestDelete, self).get_object(*args, **kwargs)
		if not obj.owner == self.request.user.c_owner:
			raise Http404
		return obj


####################################################################################
# Submission CRUD

# Submission Creation
class SubmissionCreate(LoginRequiredMixin, generic.CreateView):
	login_url = '/user/login/'
	form_class = SubmissionForm
	model = Submission
	template_name = 'contests/_form_submission.html'

	def get(self, request, *args, **kwargs):
		self.contest = get_object_or_404(Contest, slug=self.kwargs['contest_slug'])
		
		# if the request user has already made a submission to the contest
		if self.contest.submission_set.filter(applicant=self.request.user).exists():
			raise Http404 # this is going to be replaced with an error message

		return super(SubmissionCreate, self).get(request, *args, **kwargs)

	def form_valid(self, form, **kwargs):
		form.instance.applicant = self.request.user
		form.instance.contest = Contest.objects.get(slug=self.kwargs['contest_slug'])
		return super(SubmissionCreate, self).form_valid(form)

# Submission Detail
class SubmissionDetail(LoginRequiredMixin, generic.DetailView):
	login_url = '/user/login/'
	model = Submission
	template_name = 'contests/details_submission.html'

	def get_object(self, *args, **kwargs):
		obj = super(SubmissionDetail, self).get_object(*args, **kwargs)

		# if request.user is a contest owner
		if self.request.user.groups.filter(name="Contest Owner"):
			# but not this contests' owner
			if not obj.contest.owner == self.request.user.c_owner:
				# booyah!
				raise Http404

		# if request.user is not a contest owner
		else:
			# but he/she is not also the applicant who post this submssion
			if not obj.applicant == self.request.user:
				# booyah! (even u are an admin :D)
				raise Http404

		return obj

# Submission Update
class SubmissionUpdate(LoginRequiredMixin, generic.UpdateView):
	login_url = '/user/login/'
	form_class = SubmissionForm
	model = Submission
	template_name = 'contests/_form_submission.html'

	# Check the submission
	def get(self, request, *args, **kwargs):
		self.contest = get_object_or_404(Contest, slug=self.kwargs['contest_slug'])
		return super(SubmissionUpdate, self).get(request, *args, **kwargs)

	# Make sure request.user is the owner of it
	def get_object(self, *args, **kwargs):
		obj = super(SubmissionUpdate, self).get_object(*args, **kwargs)
		if not obj.applicant == self.request.user:
			raise Http404
		return obj

	def form_valid(self, form, **kwargs):
		return super(SubmissionUpdate, self).form_valid(form)
		
# Submission Delete
class SubmissionDelete(LoginRequiredMixin, generic.DeleteView):
	login_url = '/user/login/'
	model = Submission
	template_name = 'contests/_form_contest_delete.html'
	success_url = reverse_lazy('contests:index')

	# Check the submission
	def get(self, request, *args, **kwargs):
		self.contest = get_object_or_404(Contest, slug=self.kwargs['contest_slug'])
		return super(SubmissionDelete, self).get(request, *args, **kwargs)

	# Make sure request.user is the owner of it
	def get_object(self, *args, **kwargs):
		obj = super(SubmissionDelete, self).get_object(*args, **kwargs)
		if not obj.applicant == self.request.user:
			raise Http404
		return obj

####################################################################################

# Submission Feedback
class FeedbackCreate(LoginRequiredMixin, generic.UpdateView):
	login_url = '/user/login/'
	model = Submission
	form_class = FeedbackForm
	template_name = 'contests/_form_submission_feedback.html'

	# Check the contest
	def get(self, request, *args, **kwargs):
		self.submission = get_object_or_404(Submission, pk=self.kwargs['pk'])
		return super(FeedbackCreate, self).get(request, *args, **kwargs)

	# Make sure request.user is the contest owner of it
	def get_object(self, *args, **kwargs):
		obj = super(FeedbackCreate, self).get_object(*args, **kwargs)
		if obj.applicant == self.request.user:
			raise Http404
		if not obj.contest.owner == self.request.user.c_owner:
			raise Http404
		return obj

	def form_valid(self, form):
		return super(FeedbackCreate, self).form_valid(form)


# Winner Form
class ContestWinner(LoginRequiredMixin, generic.CreateView):
	login_url = '/user/login/'
	model = Winner
	form_class = WinnerForm
	template_name = 'contests/_form_contest_winner.html'

	# Check the contest
	def get(self, request, *args, **kwargs):
		self.contest = get_object_or_404(Contest, slug=self.kwargs['slug'])
		if not self.request.user.groups.filter(name="Contest Owner"):
			raise Http404
		if not self.contest.owner == self.request.user.c_owner:
			raise Http404
		return super(ContestWinner, self).get(request, *args, **kwargs)

	def get_context_data(self, *args, **kwargs):
		context = super(ContestWinner, self).get_context_data(*args, **kwargs)
		context['form'].fields['winner'].queryset = Submission.objects.filter(contest__slug=self.kwargs['slug'])
		return context

	def form_valid(self, form):
		form.instance.contest = Contest.objects.get(slug=self.kwargs['slug'])
		return super(ContestWinner, self).form_valid(form)
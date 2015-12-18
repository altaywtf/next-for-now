#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Category, Contest, Submission
from nfn_user.models import C_Owner

from .forms import ContestForm, SubmissionForm

####################################################################################
# Contest Listing

# Contest Listing: List All
class IndexView(generic.ListView):
	template_name = 'contests/index.html'
	context_object_name = 'contest_list'
	allow_empty = True

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
	template_name = 'contests/index.html'
	context_object_name = 'contest_list'

	def get_queryset(self):
		self.category = get_object_or_404(Category, slug=self.kwargs['category_slug'])
		return Contest.objects.filter(category__slug=self.kwargs['category_slug'], is_approved=True).order_by('-date_started')

	def get_context_data(self, *args, **kwargs):
		context = super(FilterByCategory, self).get_context_data(*args, **kwargs)
		context['contest_category_list'] = Category.objects.all()
		context['contest_owner_list'] = C_Owner.objects.all()
		return context

# Contest Listing: Filter by Contest Owner
class FilterByOwner(generic.ListView):
	template_name = 'contests/index.html'
	context_object_name = 'contest_list'

	def get_queryset(self):
		self.owner = get_object_or_404(C_Owner, pk=self.kwargs['company_pk'])
		return Contest.objects.filter(owner_id=self.kwargs['company_pk'], is_approved=True).order_by('-date_started')

	def get_context_data(self, *args, **kwargs):
		context = super(FilterByOwner, self).get_context_data(*args, **kwargs)
		context['contest_category_list'] = Category.objects.all()
		context['contest_owner_list'] = C_Owner.objects.all()
		return context


####################################################################################
# Contest CRUD

# Contest Creation -accessible only for c_owner accounts-
class ContestCreate(generic.CreateView):
	form_class = ContestForm
	model = Contest
	template_name = 'contests/_form_contest.html'

	def form_valid(self, form):
		form.instance.owner = self.request.user.c_owner
		return super(ContestCreate, self).form_valid(form)

# Contest Detail View
class ContestDetail(generic.DetailView):
	model = Contest
	template_name = 'contests/details_contest.html'
	slug_field = 'slug'

# Contest Update -accesible only for contest owner-
class ContestUpdate(generic.UpdateView):
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
class ContestDelete(generic.DeleteView):
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
	redirect_field_name = 'redirect_to'
	form_class = SubmissionForm
	model = Submission
	template_name = 'contests/_form_submission.html'

	def get(self, request, *args, **kwargs):
		self.contest = get_object_or_404(Contest, slug=self.kwargs['contest_slug'])
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
		form.instance.applicant = self.request.user
		form.instance.contest = Contest.objects.get(slug=self.kwargs['contest_slug'])
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
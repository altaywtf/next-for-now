from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.views import generic

from .models import Category, Contest, Submission
from nfn_user.models import C_Owner

from .forms import ContestForm, SubmissionForm

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

class FilterByCategory(generic.ListView):
	template_name = 'contests/index.html'
	context_object_name = 'contest_list'

	def get_queryset(self):
		return Contest.objects.filter(category='Design', is_approved=True).order_by('-date_started')

	def get_context_data(self, *args, **kwargs):
		context = super(FilterByCategory, self).get_context_data(*args, **kwargs)
		context['contest_category_list'] = Category.objects.all()
		context['contest_owner_list'] = C_Owner.objects.all()
		return context


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


class ContestDetail(generic.DetailView):
	model = Contest
	template_name = 'contests/details_contest.html'



class ContestCreate(generic.CreateView):
	form_class = ContestForm
	model = Contest
	template_name = 'contests/_form_contest.html'
	success_url = '/contests/'

	def form_valid(self, form):
		form.instance.owner = self.request.user.c_owner
		return super(ContestCreate, self).form_valid(form)

class ContestUpdate(generic.UpdateView):
	form_class = ContestForm
	model = Contest
	template_name = 'contests/_form_contest.html'
	success_url = '/contests/'

	def get_object(self, *args, **kwargs):
		obj = super(ContestUpdate, self).get_object(*args, **kwargs)
		if not obj.owner == self.request.user.c_owner:
			raise Http404
		return obj

	def form_valid(self, form):
		form.instance.owner = self.request.user.c_owner
		return super(ContestUpdate, self).form_valid(form)

class ContestDelete(generic.DeleteView):
	model = Contest
	template_name = 'contests/_form_contest_delete.html'
	success_url = '/contests/'

	def get_object(self, *args, **kwargs):
		obj = super(ContestDelete, self).get_object(*args, **kwargs)
		if not obj.owner == self.request.user.c_owner:
			raise Http404
		return obj



class SubmissionCreate(generic.CreateView):
	form_class = SubmissionForm
	model = Submission
	template_name = 'contests/_form_submission.html'
	success_url = '/contests/'

	def get(self, request, *args, **kwargs):
		self.contest = get_object_or_404(Contest, pk=self.kwargs['contest_pk'])
		return super(SubmissionCreate, self).get(request, *args, **kwargs)

	def form_valid(self, form, **kwargs):
		form.instance.applicant = self.request.user
		form.instance.contest = Contest.objects.get(pk=self.kwargs['contest_pk'])
		return super(SubmissionCreate, self).form_valid(form)


class SubmissionDetail(generic.DetailView):
	model = Submission
	template_name = 'contests/details_submission.html'

	def get_object(self, *args, **kwargs):
		obj = super(SubmissionDetail, self).get_object(*args, **kwargs)

		if self.request.user.groups.all()[0].name == "Contest Owner":
			if not obj.contest.owner == self.request.user.c_owner:
				raise Http
		
		else:
			if not obj.applicant == self.request.user:
				raise Http404

		return obj


class SubmissionUpdate(generic.UpdateView):
	form_class = SubmissionForm
	model = Submission
	template_name = 'contests/_form_submission.html'
	success_url = '/contests/'

	def get(self, request, *args, **kwargs):
		self.contest = get_object_or_404(Contest, pk=self.kwargs['contest_pk'])
		return super(SubmissionUpdate, self).get(request, *args, **kwargs)

	def get_object(self, *args, **kwargs):
		obj = super(SubmissionUpdate, self).get_object(*args, **kwargs)
		if not obj.applicant == self.request.user:
			raise Http404
		return obj

	def form_valid(self, form, **kwargs):
		form.instance.applicant = self.request.user
		form.instance.contest = Contest.objects.get(pk=self.kwargs['contest_pk'])
		return super(SubmissionUpdate, self).form_valid(form)
		

class SubmissionDelete(generic.DeleteView):
	model = Submission
	template_name = 'contests/_form_contest_delete.html'
	success_url = '/contests/'

	def get_object(self, *args, **kwargs):
		obj = super(SubmissionDelete, self).get_object(*args, **kwargs)
		if not obj.applicant == self.request.user:
			raise Http404
		return obj

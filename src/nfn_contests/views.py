from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.views import generic

from .models import Contest, Submission
from nfn_user.models import C_Owner

from .forms import ContestCreationForm, ContestUpdateForm

class IndexView(generic.ListView):
	template_name = 'contests/index.html'
	context_object_name = 'contest_list'

	def get_queryset(self):
		return Contest.objects.filter(is_approved=True).order_by('-date_started')
	
	def get_context_data(self, *args, **kwargs):
		context = super(IndexView, self).get_context_data(*args, **kwargs)
		context['contest_category_list'] = Contest.objects.get(pk=1).get_categories
		context['contest_owner_list'] = C_Owner.objects.all()
		return context


class FilterByCategory(generic.ListView):
	template_name = 'contests/index.html'
	context_object_name = 'contest_list'

	def get_queryset(self):
		return Contest.objects.filter(category=self.kwargs['category_name'], is_approved=True).order_by('-date_started')

	def get_context_data(self, *args, **kwargs):
		context = super(FilterByCategory, self).get_context_data(*args, **kwargs)
		context['contest_category_list'] = Contest.objects.get(pk=1).get_categories
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
		context['contest_category_list'] = Contest.objects.get(pk=1).get_categories
		context['contest_owner_list'] = C_Owner.objects.all()
		return context


class ContestDetailView(generic.DetailView):
	model = Contest
	template_name = 'contests/details.html'


class ContestCreate(generic.CreateView):
	form_class = ContestCreationForm
	model = Contest
	template_name = 'contests/create.html'
	success_url = '/contests/'

	def form_valid(self, form):
		form.instance.owner = self.request.user.c_owner
		return super(ContestCreate, self).form_valid(form)

class ContestUpdate(generic.UpdateView):
	form_class = ContestUpdateForm
	model = Contest
	template_name = 'contests/update.html'
	success_url = '/contests/'

	def get_object(self, *args, **kwargs):
		obj = super(ContestUpdate, self).get_object(*args, **kwargs)
		if not obj.owner == self.request.user.c_owner:
			raise Http404
		return obj

	def form_valid(self, form):
		form.instance.owner = self.request.user.c_owner
		return super(ContestUpdate, self).form_valid(form)



''' class ContestDelete(generic.DeleteView): '''

''' class EditView(): '''

''' class ApplyView(): '''

''' class SubmissionsView(): '''

''' class ViewSubmissionView(): '''
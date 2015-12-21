from django.conf.urls import url

from . import views

app_name = 'contests'

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),	
	url(r'^category/(?P<category_slug>[\w-]+)/$', views.FilterByCategory.as_view(), name='by_category'),
	url(r'^company/(?P<company_pk>[\w-]+)/$', views.FilterByOwner.as_view(), name='by_owner'),
	url(r'^ongoing/$', views.FilterByOngoing.as_view(), name='by_ongoing'),
	url(r'^finished/$', views.FilterByFinished.as_view(), name='by_finished'),
	url(r'^search/$', views.FilterBySearch.as_view(), name='by_search'),
	
	url(r'^create/$', views.ContestCreate.as_view(), name='create_contest'),
	url(r'^(?P<slug>[\w-]+)/update/$', views.ContestUpdate.as_view(), name='update_contest'),
	url(r'^(?P<slug>[\w-]+)/delete/$', views.ContestDelete.as_view(), name='delete_contest'),
	url(r'^(?P<slug>[\w-]+)/$', views.ContestDetail.as_view(), name='view_contest'),
	url(r'^(?P<slug>[\w-]+)/winner/$', views.ContestWinner.as_view(), name='contest_winner'),

	url(r'^(?P<contest_slug>[\w-]+)/apply/$', views.SubmissionCreate.as_view(), name='post_submission'),
	url(r'^(?P<contest_slug>[\w-]+)/submissions/(?P<pk>[0-9]+)/update/$', views.SubmissionUpdate.as_view(), name='update_submission'),
	url(r'^(?P<contest_slug>[\w-]+)/submissions/(?P<pk>[0-9]+)/delete/$', views.SubmissionDelete.as_view(), name='delete_submission'),
	url(r'^(?P<contest_slug>[\w-]+)/submissions/(?P<pk>[0-9]+)/$', views.SubmissionDetail.as_view(), name='view_submission'),

	url(r'^(?P<contest_slug>[\w-]+)/submissions/(?P<pk>[0-9]+)/feedback/$', views.FeedbackCreate.as_view(), name='submission_feedback')
]
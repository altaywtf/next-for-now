from django.conf.urls import url

from . import views

app_name = 'contests'

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),	
	url(r'^category/(?P<category_pk>[\w-]+)/$', views.FilterByCategory.as_view(), name='by_category'),
	url(r'^(?i)company/(?P<company_pk>[\w-]+)/$', views.FilterByOwner.as_view(), name='by_owner'),
	
	url(r'^create/$', views.ContestCreate.as_view(), name='create_contest'),
	url(r'^(?P<pk>[0-9]+)/update/$', views.ContestUpdate.as_view(), name='update_contest'),
	url(r'^(?P<pk>[0-9]+)/delete/$', views.ContestDelete.as_view(), name='delete_contest'),
	url(r'^(?P<pk>[0-9]+)/$', views.ContestDetail.as_view(), name='view_contest'),

	url(r'^(?P<contest_pk>[0-9]+)/apply/$', views.SubmissionCreate.as_view(), name='post_submission'),
	url(r'^(?P<contest_pk>[0-9]+)/submissions/(?P<pk>[0-9]+)/update/$', views.SubmissionUpdate.as_view(), name='update_submission'),
	url(r'^(?P<contest_pk>[0-9]+)/submissions/(?P<pk>[0-9]+)/delete/$', views.SubmissionDelete.as_view(), name='delete_submission'),
	url(r'^(?P<contest_pk>[0-9]+)/submissions/(?P<pk>[0-9]+)$', views.SubmissionDetail.as_view(), name='view_submission'),
]
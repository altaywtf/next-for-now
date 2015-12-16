from django.conf.urls import url

from . import views

app_name = 'contests'

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	
	url(r'^(?P<pk>[0-9]+)/$', views.ContestDetailView.as_view(), name='detail'),
	
	url(r'^category/(?P<category_name>[\w-]+)/$', views.FilterByCategory.as_view(), name='by_category'),
	url(r'^company/(?P<company_pk>[\w-]+)/$', views.FilterByOwner.as_view(), name='by_owner'),
	
	url(r'^create/$', views.ContestCreate.as_view(), name='create_contest'),
	url(r'^(?P<pk>[0-9]+)/update/$', views.ContestUpdate.as_view(), name='update_contest'),
	url(r'^(?P<pk>[0-9]+)/delete/$', views.ContestDelete.as_view(), name='delete_contest'),
]
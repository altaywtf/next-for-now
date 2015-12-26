from django.conf.urls import url
from . import views

app_name = 'user'

urlpatterns = [
	url(r'^signup/$', views.SignUpView, name='signup'),
    url(r'^signup/cowner/$', views.cOwnerSignUpView, name='signup_cowner'),
    url(r'^signup/applicant/$', views.applicantSignUpView, name='signup_applicant'),
    url(r'^login/$', views.loginView, name='login'),
    url(r'^logout/$', views.logoutView, name='logout'),
    url(r'^settings/$', views.userChangeView, name='settings'),
    url(r'^password/reset/$', 'django.contrib.auth.views.password_reset', {'post_reset_redirect': '/user/password/reset/done/$'},
    	name="password_reset"),
    url(r'^password/reset/done/$', 'django.contrib.auth.views.password_reset_done'),
    url(r'^user/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 
        'django.contrib.auth.views.password_reset_confirm', 
        {'post_reset_redirect' : '/user/password/done/'}),
    url(r'^user/password/done/$', 
        'django.contrib.auth.views.password_reset_complete'),
]
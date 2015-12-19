from django.conf.urls import url
from . import views

app_name = 'user'

urlpatterns = [
    url(r'^signup/cowner/$', views.cOwnerSignUpView, name='signup_cowner'),
    url(r'^signup/applicant/$', views.applicantSignUpView, name='signup_applicant'),
    url(r'^login/$', views.loginView, name='login'),
    url(r'^logout/$', views.logoutView, name='logout')
]


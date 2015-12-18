from django.conf.urls import url
from . import views

app_name = 'user'

urlpatterns = [
    url(r'^signup/cowner/$', views.cOwnerSignUpView),
    url(r'^signup/applicant/$', views.applicantSignUpView),
    url(r'^login/$', views.loginView),
    url(r'^logout/$', views.logoutView)
]


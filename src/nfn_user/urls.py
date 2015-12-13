from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^cowner/$', views.cOwnerSignUpView)
]


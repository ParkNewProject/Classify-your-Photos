from django.urls import path
from django.conf.urls import url
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
   url(r'^signup/$', views.signup, name='signup'),
   url(r'^login/$', views.login, name='login'),
   url(r'^logout/$', views.logout, name='logout'),
    # ex: /user/signup/
]

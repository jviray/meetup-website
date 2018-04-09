"""Defines URL patterns for user_accounts."""

from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
	# Login page
	url(r'^login/$', login, {'template_name': 'user_accounts/login.html'},
		name='login'),
	# Sign up page
	url(r'^signup/$', views.signup, name='signup'),
	# Logout page
	url(r'^logout/$', views.logout_view, name='logout'),
	url(r'^profile/$', views.profile, name='profile'),
]
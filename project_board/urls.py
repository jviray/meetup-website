"""Defines URLS patterns for the project board."""

from django.conf.urls import url

from . import views

urlpatterns = [
	# Show all projects
	url(r'^$', views.projects, name='projects'),
]
from django.shortcuts import render

from .models import Project

def projects(request):
	"""Show all projects."""
	projects = Project.objects.order_by('posted')
	context = {'projects': projects}
	return render(request, 'project_board/projects.html', context)
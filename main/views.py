from django.shortcuts import render

def home(request):
	"""The home page for our website"""
	return render(request, 'main/home.html')
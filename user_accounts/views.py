from django.shortcuts import render

def index(request):
	"""The home page for our website"""
	return render(request, 'user_accounts/index.html')
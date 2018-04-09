from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.CharField(max_length=100, blank=True)
	skills = models.CharField(max_length=100, blank=True)
	website = models.URLField(blank=True)
	# Add projects, contact, github


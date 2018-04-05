from django.db import models

class Project(models.Model):
	title = models.CharField(max_length=200)
	posted = models.DateTimeField(auto_now_add=True)
	description = models.TextField()
	contact_email = models.EmailField(max_length=254, blank=True)

	def __str__(self):
		"""Return a string reprsentation of the model."""
		return self.title
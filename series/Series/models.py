from django.db import models


class Serie(models.Model):
	title = models.CharField(max_length=100, help_text='title of Serie')
	description = models.TextField(max_length=255,help_text="Description of Serie")
	
	def __str__(self):
		return self.title
		
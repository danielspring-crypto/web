from django.db import models

# Create your models here

class Post(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	username = models.CharField(max_length=255)
	uploaded_time = models.DateTimeField()

	def __str__(self):
		return self.title 
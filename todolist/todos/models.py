from django.db import models
from datetime import datetime

class Todo(models.Model):
	text = models.CharField(max_length=115)
	complete = models.BooleanField(default=False)
	def __str__(self):
		return self.text
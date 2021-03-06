from django.db import models

class Contact(models.Model):
	first_name=models.CharField(max_length=20)
	last_name=models.CharField(max_length=20)
	email=models.EmailField()
	number=models.PositiveIntegerField()
	def __str__(self):
		return ' '.join([
			self.first_name,
			self.last_name
		])

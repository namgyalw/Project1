from django.db import models

# Create your models here.
class Student(models.Model):
	Name = models.CharField(max_length=100, blank=True)
	Gender = models.CharField(max_length=100, blank=True)
	Age = models.CharField(max_length=100, blank=True)
	Grade = models.CharField(max_length=100, blank=True)

	def __str__(self):
		return self.Name

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Dog(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	breed = models.CharField(max_length=100)
	thiccness = models.CharField(max_length=120)
	age = models.IntegerField()

	def __str__(self):
		return self.name
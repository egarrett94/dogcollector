from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Dog(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	breed = models.CharField(max_length=100)
	thiccness = models.CharField(max_length=120)
	age = models.IntegerField()
	likes = models.IntegerField(default=0)

	def __str__(self):
		return self.name

class Toy(models.Model):
	name = models.CharField(max_length=100)
	dogs = models.ManyToManyField(Dog)

	def __str__(self):
		return self.name
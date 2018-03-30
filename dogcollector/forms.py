from django import forms
from .models import Dog

class DogForm(forms.ModelForm):

	class Meta:
		model = Dog
		fields = ['name', 'breed', 'thiccness', 'age']

	# name = forms.CharField(label='Name', max_length=100)
	# breed = forms.CharField(label='Breed', max_length=100)
	# thiccness = forms.CharField(label='Thiccness', max_length=100)
	# age = forms.IntegerField(label='Age')
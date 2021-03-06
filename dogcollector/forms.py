from django import forms
from .models import Dog, User, Toy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class DogForm(forms.ModelForm):

	class Meta:
		model = Dog
		fields = ['name', 'breed', 'thiccness', 'age']

	# name = forms.CharField(label='Name', max_length=100)
	# breed = forms.CharField(label='Breed', max_length=100)
	# thiccness = forms.CharField(label='Thiccness', max_length=100)
	# age = forms.IntegerField(label='Age')

class LoginForm(forms.Form):
	username = forms.CharField(label='User Name', max_length=64)
	password = forms.CharField(widget=forms.PasswordInput())

class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length = 30, required=False)
	last_name = forms.CharField(max_length = 50, required=False)
	email = forms.EmailField(max_length = 254, help_text='email is required')

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
	
class ToyForm(forms.ModelForm):
	class Meta: 
		model = Toy 
		fields = ('name',)
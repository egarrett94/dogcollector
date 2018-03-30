from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Dog
from .forms import DogForm
from django.contrib.auth.models import User

# Create your views here.
## DUMMY DATA ## 
# class Dog:
# 	def __init__(self, name, breed, thiccness, age):
# 		self.name = name
# 		self.breed = breed
# 		self.thiccness = thiccness
# 		self.age = age 
# 	def __str__(self):
# 		return self.name

# doggos = [
# 	Dog('Judas', 'puggo', 'af', 7),
# 	Dog('Lucas', 'mutt', 'none', 0),
# 	Dog('Zeo', 'chihuahua', 'no thicc', 2),
# 	Dog('Buddy', 'golden lab', 'so many', 9)
# ]

def index(request):
	dogs = Dog.objects.all()
	# return HttpResponse('<h1>holla</h1>')
	form = DogForm()
	return render(request, 'index.html', {'doggos': dogs, 'form': form})
	# render( request, template, context )

def show(request, dog_id):
	dog = Dog.objects.get(id=dog_id)
	return render(request, 'show.html', {'dog': dog})

def post_dog(request):
	form = DogForm(request.POST)
	if form.is_valid():
		# dog = Dog(
		# 	name=form.cleaned_data['name'],
		# 	breed=form.cleaned_data['breed'],
		# 	thiccness=form.cleaned_data['thiccness'],
		# 	age=form.cleaned_data['age']
		# )

		#creates the dog but doesn't actually save it 
		#because when the form is submitted it needs to add
		# the user to the dog object
		dog = form.save(commit=False)
		dog.user = request.user
		dog.save()
	return HttpResponseRedirect('/')

def profile(request, username):
	user = User.objects.get(username=username)
	# grabs all dogs associated w this particular user
	dogs = Dog.objects.filter(user=user)
	return render(request, 'profile.html', {'username': username, 'dogs': dogs})

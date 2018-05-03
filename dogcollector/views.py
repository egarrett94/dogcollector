import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Dog, Toy
from .forms import DogForm, LoginForm, SignUpForm, ToyForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

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
	form = ToyForm()
	return render(request, 'show.html', {'dog': dog, 'form':form})

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

def login_view(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			u = form.cleaned_data['username']
			p = form.cleaned_data['password']
			user = authenticate(username = u, password = p)
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect('/')
				else: 
					print('This account has been disabled.')
			else: 
				print('The username and/or password is incorrect.')
	else: 
		form = LoginForm()
	return render(request, 'login.html', { 'form': form } )

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid(): 
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return HttpResponseRedirect('/')
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form':form})

def like_dog(request):
	dog_id = request.GET.get('dog_id', None)
	likes = 0
	if (dog_id):
		dog = Dog.objects.get(id=int(dog_id))
		if dog is not None:
			likes = dog.likes + 1
			dog.likes = likes
			dog.save()
	return HttpResponse(likes)

def edit_dog(request, dog_id):
	#query database, find cat or send 404 if no cat 
	instance = get_object_or_404(Dog, id=dog_id)
	#use dogform to plug in instance 
	form = DogForm(request.POST or None, instance=instance)
	if form.is_valid():
		form.save()
		return redirect('show', dog_id)
	else: 
		return render(request, 'edit_dog.html', {'dog': instance, 'form': form});

def delete_dog(request, dog_id):
	if request.method == 'POST':
		instance = Dog.objects.get(pk=dog_id)
		instance.delete()
		return redirect('index')

def create_toy(request, dog_id):
	form = ToyForm(request.POST)
	if form.is_valid():
		try: 
			toy = Toy.objects.get(name=form.data.get('name'))
		except: 
			toy = None 
		if toy is None:
			toy = form.save()
		dog = Dog.objects.get(pk=dog_id)
		toy.dogs.add(dog)
		return redirect('show_toy', toy.id)
	else: 
		return redirect('show', dog_id)

def show_toy(request, toy_id):
	toy = Toy.objects.get(pk=toy_id)
	dogs = toy.dogs.all()
	return render(request, 'show_toy.html', {'toy': toy})

def api(request):
	payload = {'key', 'Mjk0MTkz'}
	res = requests.get('http://thecatapi.com/api/images/get', params=payload)
	return render(request, 'api.html', {'image': res.url})







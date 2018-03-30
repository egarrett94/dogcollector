from django.urls import path, re_path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	# path( url/, view, kwargs, name )
	# re_path(r'^([0-9]+)/$', views.show, name='show')
	path('<int:dog_id>/', views.show, name='show'),
	path('post_dog/', views.post_dog, name='post_dog'),
	path('user/<username>', views.profile, name='profile')
]
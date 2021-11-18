from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm 
from django.urls import reverse_lazy
from django.views import generic  
from django.views.generic import CreateView
from .models import Person 
from django.contrib.auth.models import User


class SignUpView(generic.CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'registration/signup.html'
	model = User 







# class SignUpView(CreateView):
# 	model = Person 
# 	template_name = 'registration/signup.html'
# 	success_url = reverse_lazy('login')
# 	fields = ['usrename', 'email', 'password']
#     
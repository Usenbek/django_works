from django.shortcuts import render
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout



# Create your views here.
def register_view(request):
  if request.method == 'GET':
    form_obj = RegisterForm()
    return render(request, 'users/register.html', context={'form': form_obj})
  elif request.method == 'POST': 
    form_obj = RegisterForm(request.POST)
    if form_obj.is_valid():
      form_obj.cleaned_data.__delitem__('confirm_password')
      User.objects.create_user('confirm_password')
      return HttpResponse("User created")
    return HttpResponse("Form is not valid")
def login_view(request):
    if request.method == 'GET':
      forms_obj = LoginForm()
      return render(request, 'users/login.html', context={'form': forms_obj})
    elif request.method == 'POST':
      forms_obj = LoginForm(request.POST)
      if forms_obj.is_valid():
        user = authenticate(**forms_obj.cleaned_data)
        login(request, user)
        return HttpResponse("You are logged in")
      
@login_required(login_url='/login/')      
def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return HttpResponse("You are logged out")
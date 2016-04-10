from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def register(request):
    form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def register_process(request):
    new_user_form = UserCreationForm(request.POST or None)
    if new_user_form.is_valid():
        new_user_form.save()
        return redirect(reverse('register_success'))
    return render(request, 'register.html', {'form': new_user_form})

def register_success(request):
    return render(request, 'register-success.html')

def sign_in(request):
    form = AuthenticationForm()
    return render(request, 'sign-in.html', {'form': form})

def sign_in_process(request):
    form = AuthenticanFomr(data=request.POST or None)
    if form.is_valid():
        login(request, form.get_user())
        return redirect('/')
    return render(request, 'sign-in.html', {'form': form})

def sign_out(request):
    logout(request)
    return redirect('/')

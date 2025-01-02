from django.shortcuts import render, redirect
from . import forms 


from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages 


def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account Create Successfully')
            return redirect('register')
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'register.html', {'form' : register_form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name, password= user_pass)
            
            if user is not None:
                messages.success(request, 'Login in Successfully')
                login(request, user)
                return redirect('homepage')
            else:
                messages.warning(request, "Login information incorrect")
                return redirect('register')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form' : form })

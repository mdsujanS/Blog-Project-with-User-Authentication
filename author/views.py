from django.shortcuts import render, redirect
from . import forms 

from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.forms import AuthenticationForm

# def add_author(request):
#     if request.method == 'POST':
#         author_form = forms.AuthorForm(request.POST)
#         if author_form.is_valid():
#             author_form.save()
#             return redirect('add_author')
#     else:
#         author_form = forms.AuthorForm()
        
#     return render(request, 'add_author.html', {'form' : author_form})

def add_author(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account Create Successfully')
            return redirect('login')
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'add_author.html', {'form' : register_form, 'type' : 'Register'})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name, password= user_pass)
            
            if user is not None:
                messages.success(request, 'Logged in Sucessfully')
                login(request, user)
                return redirect('homepage')
            else:
                messages.warning(request, "Login information incorrect")
                return redirect('add_author')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form' : form })

from django.shortcuts import render, redirect
from . import forms 

from django.contrib import messages 

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
            return redirect('add_author')
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'add_author.html', {'form' : register_form, 'type' : 'Register'})
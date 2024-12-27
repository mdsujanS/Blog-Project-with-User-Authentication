from django.shortcuts import render 
from Post.models import Post 

def home(request):
    allPost = Post.objects.all()
    return render(request, 'home.html', {'allPost': allPost})

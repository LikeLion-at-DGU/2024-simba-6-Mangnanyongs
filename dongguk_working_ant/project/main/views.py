from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Post

# Create your views here.
def mainpage(request):
    posts = Post.objects.all()
    return render(request, 'main/mainpage.html', {'posts':posts})

def mainlistpage(request):
    posts = Post.objects.all()
    return render(request, 'main/mainlistpage.html', {'posts':posts})
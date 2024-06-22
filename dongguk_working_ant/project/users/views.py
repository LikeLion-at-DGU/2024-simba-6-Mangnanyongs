from django.shortcuts import render, redirect, get_object_or_404
from main.models import Post

# Create your views here.
def staff_mypage(request):
    return render(request, 'users/staff_mypage.html')

def staff_appslist(request):
    return render(request, 'users/staff_appslist.html')

def staff_mypost(request):
    posts = Post.objects.filter(writer=request.user.id)
    return render(request, 'users/staff_mypost.html', {'posts':posts})

def staff_studentappfile(request):
    return render(request, 'users/staff_studentappfile.html')

def student_myapplication(request):
    return render(request, 'users/student_myapplication.html')

def student_mypage(request):
    return render(request, 'users/student_mypage.html')

def student_myscrap(request):
    scraped_posts = request.user.scraped.all()
    return render(request, 'users/student_myscrap.html', {'scraped_posts':scraped_posts})

def student_mywork(request):
    return render(request, 'users/student_mywork.html')
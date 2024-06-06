from django.shortcuts import render, redirect
from django.contrib import auth
from .models import Profile_Staff, Profile_Student
from django.contrib.auth.models import User

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('main:mainpage')
        else:
            return render(request,'accounts/login.html')

    elif request.method == 'GET':
        return render(request, 'accounts/login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('main:mainpage')

def signup_choose(request):
    return render(request, 'accounts/signup_choose.html')

def signup_student(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm']:
            user = User.objects.create_user(
                username = request.POST['username'],
                password = request.POST['password'],
            )

            name = request.POST['name']
            gender = request.POST['gender']
            birth = request.POST['birth']
            department = request.POST['department']
            phone = request.POST['phone']
            email = request.POST['email']
            if request.FILES.get('certification'):
                certification = request.FILES['certification']

            profile_student = Profile_Student(user=user, name=name, gender=gender, birth=birth, department=department, phone=phone, email=email)
            if request.FILES.get('certification'):
                profile_student = Profile_Student(certification=certification)
            profile_student.save()

            auth.login(request, user)
            return redirect('/')

    return render(request, 'accounts/signup_student.html')

def signup_staff(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm']:
            user = User.objects.create_user(
                username = request.POST['username'],
                password = request.POST['password'],
            )

            name = request.POST['name']
            email = request.POST['email']
            if request.FILES.get('certification'):
                certification = request.FILES['certification']

            profile_staff = Profile_Staff(user=user, name=name, email=email)
            if request.FILES.get('certification'):
                profile_staff = Profile_Staff(certification=certification)

            profile_staff.save()

            auth.login(request, user)
            return redirect('/')

    return render(request, 'accounts/signup_staff.html')

from django.shortcuts import render, redirect
from django.contrib import auth
from .models import Profile
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

            student_or_staff = 'student'
            name = request.POST['name']
            gender = request.POST['gender']
            birth = request.POST['birth']
            department = request.POST['department']
            phone = request.POST['phone']
            email = request.POST['email']
            photo = request.POST['photo']
            if request.FILES.get('certification_student'):
                certification = request.FILES['certification_student']

            profile = Profile(student_or_staff=student_or_staff, user=user, name=name, gender=gender, birth=birth, department=department, phone=phone, email=email, photo=photo)
            if request.FILES.get('certification_student'):
                profile = Profile(certification=certification)
            profile.save()

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

            student_or_staff = 'staff'
            name = request.POST['name']
            email = request.POST['email']
            if request.FILES.get('certification_staff'):
                certification = request.FILES['certification_staff']

            profile = Profile(student_or_staff=student_or_staff, user=user, name=name, email=email)
            if request.FILES.get('certification_staff'):
                profile = Profile(certification=certification)

            profile.save()

            auth.login(request, user)
            return redirect('/')

    return render(request, 'accounts/signup_staff.html')

def delete_account(request):
    request.user.delete()
    return redirect('main:mainlistpage')
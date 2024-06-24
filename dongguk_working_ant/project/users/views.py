from django.shortcuts import render, redirect, get_object_or_404
from main.models import Post, Application, Answer
from django.contrib.auth.models import User

# Create your views here.
def staff_mypage(request):
    return render(request, 'users/staff_mypage.html')

#지원한 학생 리스트 페이지
def staff_appslist(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    applications = Application.objects.filter(post_id=post_id).select_related('writer')
    students = [app.writer for app in applications]
    return render(request, 'users/staff_appslist.html',{'students':students, 'post':post})

def staff_mypost(request):
    posts = Post.objects.filter(writer=request.user.id)
    return render(request, 'users/staff_mypost.html', {'posts':posts})

#학생 지원서 내용 페이지
def staff_studentappfile(request, post_id, student_id):
    application = get_object_or_404(Application, writer_id=student_id, post_id=post_id)
    student = get_object_or_404(User, id=student_id)
    answers = Answer.objects.filter(application=application)
    return render(request, 'users/staff_studentappfile.html',{'appcliation':application, 'answers':answers, 'student':student})

def student_myapplication(request):
    if request.user.is_authenticated:
        applications = Application.objects.filter(writer=request.user)
        applications = applications.order_by('-is_accepted')
        return render(request, 'users/student_myapplication.html', {'applications':applications})
    return redirect('accounts:login')

def student_mypage(request):
    return render(request, 'users/student_mypage.html')

def student_myscrap(request):
    scraped_posts = request.user.scraped.all()
    post_data = []

    for post in scraped_posts:
        has_application = Application.objects.filter(post=post, writer=request.user).exists()
        post_data.append({'post': post, 'has_application': has_application})

    return render(request, 'users/student_myscrap.html', {'post_data': post_data})

def student_mywork(request):
    mywork = Application.objects.filter(writer=request.user, is_accepted=2).select_related('post')
    mywork_posts = [application.post for application in mywork]
    return render(request, 'users/student_mywork.html', {'mywork_posts': mywork_posts})
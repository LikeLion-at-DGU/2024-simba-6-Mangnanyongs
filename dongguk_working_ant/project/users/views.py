from django.shortcuts import render, redirect, get_object_or_404
from main.models import Post, Application, Answer

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
    answers = Answer.objects.filter(application=application)
    return render(request, 'users/staff_studentappfile.html',{'appcliation':application, 'answers':answers})

def student_myapplication(request):
    applications = Application.objects.filter(writer=request.user).select_related('post')
    applicated_posts = [application.post for application in applications]
    return render(request, 'users/student_myapplication.html', {'applicated_posts': applicated_posts})

def student_mypage(request):
    return render(request, 'users/student_mypage.html')

def student_myscrap(request):
    scraped_posts = request.user.scraped.all()
    return render(request, 'users/student_myscrap.html', {'scraped_posts':scraped_posts})

def student_mywork(request):
    mywork = Application.objects.filter(writer=request.user, is_accepted=1).select_related('post')
    mywork_posts = [application.post for application in mywork]
    return render(request, 'users/student_mywork.html', {'mywork_posts': mywork_posts})
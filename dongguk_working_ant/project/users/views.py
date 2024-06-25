from django.shortcuts import render, redirect, get_object_or_404
from main.models import Post, Application, Answer
from accounts.models import Notice
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import JsonResponse
# Create your views here.
def staff_mypage(request):
    return render(request, 'users/staff_mypage.html')

#지원한 학생 리스트 페이지
def staff_appslist(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    applications = Application.objects.filter(post_id=post_id)
    
    return render(request, 'users/staff_appslist.html', {'applications': applications, 'post': post})

def staff_mypost(request):
    posts = Post.objects.filter(writer=request.user.id)
    return render(request, 'users/staff_mypost.html', {'posts':posts})

#학생 지원서 내용 페이지
def staff_studentappfile(request, post_id, student_id):
    post = get_object_or_404(Post, pk=post_id)
    application = get_object_or_404(Application, writer_id=student_id, post_id=post_id)
    student = get_object_or_404(User, id=student_id)
    answers = Answer.objects.filter(application=application)
    return render(request, 'users/staff_studentappfile.html',{'appcliation':application, 'answers':answers, 'student':student, 'post':post})

def student_myapplication(request):
    #post = get_object_or_404(Post)
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

def check_result(request, post_id):
    if request.method == "POST":
        checked_applications = request.POST.getlist('check')
        
        for app in checked_applications:
            application = get_object_or_404(Application, pk=app)

            #학생에게 알림전송
            new_notice = Notice()
            new_notice.user = application.writer
            
            if request.POST.get('result')== '합격':
                application.is_accepted = 2
                new_notice.content = '합격 | [' + application.post.organization + ']' + application.post.title
            elif request.POST.get('result') == '불합격':
                application.is_accepted = 1
                new_notice.content = '불합격 | [' + application.post.organization + ']' + application.post.title
            application.save()

            new_notice.link = str(application.post.id)
            new_notice.pub_date = timezone.now()
            new_notice.save()

    return redirect('users:staff-appslist', post_id)

def notice(request):
    notices = Notice.objects.filter(user=request.user)
    notice_list = [{'summary': notice.summary(), 'link': int(notice.link)} for notice in notices]
    return JsonResponse({'notices': notice_list})

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import datetime
from django.db.models import Q, Count, F
import json
from .models import Post, Question, Application, Answer, Review
from accounts.models import Notice
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.db.models import Case, When, Value, IntegerField

# Create your views here.
def mainpage(request):
    posts = Post.objects.all()
    posts = posts.order_by('-pub_date')
    return render(request, 'main/mainpage.html', {'posts':posts})

def mainlistpage(request):
    if request.user.is_authenticated:
        
        # 입력 파라미터
        department = request.GET.get('depa','전체')
        keyword = request.GET.get('kw', '')
        sort = request.GET.get('so', '')
        end = request.GET.get('en', '')
        place = request.GET.get('pl', '')
        income = request.GET.get('inc', '')

        # 검색
        posts = Post.objects.all()

        if department == '국가':
            posts = posts.filter(department='국가')
        elif department == '교내':
            posts = posts.filter(department='교내')
        elif department == '학과':
            posts = posts.filter(~Q(department='교내'), ~Q(department='국가'), Q(department=request.user.profile.department))

        if keyword:
            posts = posts.filter(
                Q(title__icontains=keyword) |  # 제목에서 검색
                Q(organization__icontains=keyword) | #기관에서 검색
                Q(body__icontains=keyword)  # 내용에서 검색
            ).distinct()
        print(keyword)
        #마감 공고 제외 여부
        if end == 'exclude':
            posts = posts.filter(day_left__gte=0) #day_left>=0
    
        #근로 장소
        place_mapping = {
            '1': '경영/사회과학관',
            '2': '과학관',
            '3': '다향관',
            '4': '명진관',
            '5': '법학/만해관',
            '6': '본관',
            '7': '신공학관',
            '8': '남산학사',
            '9': '중앙도서관',
            '10': '원흥관',
            '11': '학림관',
            '12': '학술문화관',
            '13': '혜화관',
            '14': '기타'
        }
        if place in place_mapping:
            posts = posts.filter(place=place_mapping[place])
        
        #소득 분위 반영 여부
        if income == 'apply':
            posts = posts.filter(is_income_bracket = 1)
        elif income == 'notapply':
            posts = posts.filter(is_income_bracket = 0)

        # 정렬
        if sort == 'deadline':
            posts = posts.annotate(
                sort_deadline=Case(
                    When(day_left__lt=0, then=Value(999999)),  # 음수인 경우 큰 값 할당
                    default='day_left'  # 음수가 아닐 경우 deadline 값 사용
                )
            ).order_by('sort_deadline', '-pub_date')
        elif sort ==  'apply':
            posts = posts.order_by('-applicated_count','-pub_date')
        elif sort ==  'scrap':
            posts = posts.order_by('-scrap','-pub_date')
        else:
            posts = posts.order_by('-pub_date')
        
        context = {
            'depa': department,
            'posts': posts, 
            'kw': keyword,
            'so': sort, 
            'en': end, 
            'pl': place,
            'inc': income,
        }

        return render(request,'main/mainlistpage.html', context)
    return redirect('accounts:login')

def new_post(request):
    return render(request, 'main/new_post.html')

def post_edit(request, id):
    edit_post = get_object_or_404(Post, pk=id)

    #지원서 양식 부분
    questions = Question.objects.filter(post=id).values_list('content', flat=True)
    questions_list = list(questions)
    question_count = len(questions)

    return render(request, 'main/post_edit.html', {'post': edit_post, 'questions_list':questions_list, 'question_count':question_count})

def post_edit_modal(request):
    return render(request, 'main/post_edit_modal.html')

def post_question_create(request, num, parent_post):
    new_question = Question()
    new_question.post = parent_post
    new_question.content = request.POST['question'+str(num)]
    new_question.save()
    return new_question

def post_create(request):
    new_post = Post()

    new_post.writer = request.user
    new_post.title = request.POST['title']
    new_post.organization = request.POST['organization']
    
    new_post.department = request.POST['department']
    new_post.is_income_bracket = request.POST['is_income_bracket']
    new_post.start_date = request.POST['start_date']
    new_post.end_date = request.POST['end_date']
    new_post.deadline = request.POST['deadline']

    #남은 날짜 계산
    deadline_date = datetime.strptime(request.POST['deadline'], '%Y-%m-%d').date()
    today = timezone.now().date()
    d_day = deadline_date - today
    new_post.day_left = d_day.days

    new_post.place = request.POST['place']
    new_post.recruitment = request.POST['recruitment']
    new_post.time = request.POST['time']
    new_post.wage = request.POST['wage']

    #body부분을 리스트로 받아오기
    body_list = request.POST.getlist('body')
    new_post.set_body(body_list)  # JSON 변환 후 저장

    #new_post.file 수정 예정
    new_post.pub_date = timezone.now()
    
    new_post.save()
    
    #지원서 양식 부분
    if request.POST['question_count']:
        question_count = int(request.POST['question_count'])
        for q in range(1, question_count+1):
            post_question_create(request, q, new_post)

    return redirect('main:post-detail', new_post.id)

def post_update(request, id):
    update_post = Post.objects.get(pk=id)
    if request.user.is_authenticated and request.user == update_post.writer:
        update_post.writer = request.user
        update_post.title = request.POST['title']
        update_post.organization = request.POST['organization']
        
        update_post.department = request.POST['department']
        update_post.is_income_bracket = request.POST['is_income_bracket']
        update_post.start_date = request.POST['start_date']
        update_post.end_date = request.POST['end_date']
        update_post.deadline = request.POST['deadline']

        #남은 날짜 계산
        deadline_date = datetime.strptime(request.POST['deadline'], '%Y-%m-%d').date()
        today = timezone.now().date()
        d_day = deadline_date - today
        update_post.day_left = d_day.days

        update_post.place = request.POST['place']
        update_post.time = request.POST['time']

        recruitment_value = request.POST.get('recruitment', '')
        direct_recruitment_value = request.POST.get('direct_recruitment', '')

        if recruitment_value == 'direct' and direct_recruitment_value.isdigit():
            update_post.recruitment = int(direct_recruitment_value)
        elif recruitment_value.isdigit():
            update_post.recruitment = int(recruitment_value)
        else:
            update_post.recruitment = None

        update_post.wage = request.POST['wage']

        #body부분을 리스트로 받아오기
        body_list = request.POST.getlist('body')
        update_post.set_body(body_list)  # JSON 변환 후 저장
        
        #new_post.file 수정 예정
        update_post.pub_date = timezone.now()

        #지원서 양식 부분
        questions = Question.objects.filter(post=id)
        
        num = 1
        for q in questions: #기존에 있던 질문 수정
            q.content = request.POST['question'+str(num)]
            num += 1
            q.save()

        if int(request.POST['question_count']) > len(questions): #새로 만드는 질문 생성
            question_count = int(request.POST['question_count'])
            for q in range(num, question_count+1):
                post_question_create(request, q, update_post)

        
        update_post.save()

    return redirect('main:post-detail', update_post.id)

def post_delete(request, id):
    delete_post = Post.objects.get(pk=id)
    delete_post.delete()
    return redirect('main:mainlistpage')

def post_detail(request, post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=post_id)
        post_body_list = post.get_body()

        applications = post.applications.all()  
        applied_users = [application.writer for application in applications]
        return render(request, 'main/post_detail.html', {'post':post, 'post_body_list':post_body_list, 'applied_users': applied_users})
    return redirect('accounts:login')

def post_detail_review(request, post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=post_id)

        applications = post.applications.all()  
        applied_users = [application.writer for application in applications]  
        
        reviews = Review.objects.filter(organization=post.organization)

        return render(request, 'main/post_detail_review.html', {'post':post,'applied_users': applied_users, 'reviews':reviews})
    return redirect('accounts:login')

def scraps(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user in post.scrap.all():
        post.scrap.remove(request.user)
        post.scrap_count -= 1
        post.save()
    else:
        post.scrap.add(request.user)
        post.scrap_count += 1
        post.save()

    previous_url = request.META.get('HTTP_REFERER', 'main:mainlistpage')
    return HttpResponseRedirect(previous_url)
    
def apply(request, post_id):
    questions = Question.objects.filter(post=post_id)
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'main/apply.html', {'questions':questions, 'post':post})

def application_create(request, post_id):
    new_application = Application()

    post = get_object_or_404(Post, pk=post_id)
    new_application.post = post
    new_application.writer = request.user

    #지원자수 추가
    post.applicated_count += 1

    new_application.save()
    post.save()

    #지원서 내용 부분
    questions = Question.objects.filter(post=new_application.post)
    num=1
    for question in questions:
            new_answer = Answer()
            new_answer.application = new_application
            new_answer.question = question
            new_answer.content = request.POST['answer'+str(num)]
            new_answer.save()
            num += 1
    
    #첨부파일
    if 'file' in request.FILES:
        new_application.file = request.FILES['file']
    new_application.save()
    
    #교직원에게 알림전송
    new_notice = Notice()
    new_notice.user = post.writer
    new_notice.content = '신규 지원자 | [' + post.organization + ']' + post.title
    new_notice.link = str(post.id)
    new_notice.pub_date = timezone.now()

    new_notice.save()

    return redirect('main:post-detail', post_id)
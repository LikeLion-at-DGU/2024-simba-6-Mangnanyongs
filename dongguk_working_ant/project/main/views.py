from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.db.models import Q, Count, F

from .models import Post

# Create your views here.
def mainpage(request):
    posts = Post.objects.all()
    return render(request, 'main/mainpage.html', {'posts':posts})

def mainlistpage(request):
    if request.user.is_authenticated:
        
        # 입력 파라미터
        keyword = request.GET.get('kw', '')
        sort = request.GET.get('so', '')
        end = request.GET.get('end', '')
        place = request.GET.get('place', '')
        income = request.GET.get('income', '')

        # 검색
        if keyword:
            posts = Post.objects.filter(
                Q(title__icontains=keyword) |  # 제목에서 검색
                Q(organization__icontains=keyword) | #기관에서 검색
                Q(body__icontains=keyword)  # 내용에서 검색
            ).distinct()
        else:
            posts = Post.objects.all()

        #마감 공고 제외 여부
        if end == 'exclude':
            posts = posts.filter(day_left__gte=0) #day_left>=0
    
        #근로 장소
        if place == '경영/사회과학관':
            posts = posts.filter(place='경영/사회과학관')
        elif place == '과학관':
            posts = posts.filter(place='과학관')
        elif place == '다향관':
            posts = posts.filter(place='다향관')
        elif place == '명진관':
            posts = posts.filter(place='명진관')
        elif place == '법학/만해관':
            posts = posts.filter(place='법학/만해관')
        elif place == '본관':
            posts = posts.filter(place='본관')
        elif place == '신공학관':
            posts = posts.filter(place='신공학관')
        elif place == '남산학사':
            posts = posts.filter(place='남산학사')
        elif place == '중앙도서관':
            posts = posts.filter(place='중앙도서관')
        elif place == '원흥관':
            posts = posts.filter(place='원흥관')
        elif place == '학림관':
            posts = posts.filter(place='학림관')
        elif place == '학술문화관':
            posts = posts.filter(place='학술문화관')
        elif place == '혜화관':
            posts = posts.filter(place='혜화관')
        elif place == '기타':
            posts = posts.filter(place='기타')
        
        #소득 분위 반영 여부
        if income == 'apply':
            posts = posts.filter(is_income_bracket = 1)


        # 정렬
        if sort == 'deadline':
            posts = posts.order_by('-deadline','-pub_date')
        elif sort ==  'inquiry':
            posts = posts.order_by('-inquiry','-pub_date')
        elif sort ==  'scrap':
            posts = posts.order_by('-scrap','-pub_date')
        else:
            posts = posts.order_by('-pub_date')
        
        #페이지 나누기 추후 추가
        #paginator = Paginator(content_list,5)
        #page = request.GET.get('page','')
        #posts = paginator.get_page(page)
        
        context = {
            'posts': posts, 
            'kw': keyword,
            'so': sort, 
            'end': end, 
            'place': place,
            'income': income,
        }

        return render(request,'main/mainlistpage.html', context)
    return redirect('accounts:login')

def post_edit(request):
    return render(request, 'main/post_edit.html')

def post_detail(request, post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=post_id)
        return render(request, 'main/post_detail.html', {'post':post})
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
    return redirect('main:mainlistpage')
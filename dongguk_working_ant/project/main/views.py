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
        kw = request.GET.get('kw', '')
        so = request.GET.get('so', '')

        # 검색
        if kw:
            posts = Post.objects.filter(
                Q(title__icontains=kw) |  # 제목에서 검색
                Q(organization__icontains=kw) | #r기관에서 검색
                Q(body__icontains=kw)  # 내용에서 검색
            ).distinct()
        else:
            posts = Post.objects.all()

        # 정렬
        if so == 'deadline':
            posts = posts.order_by('-deadline','-pub_date')
        elif so ==  'inquiry':
            posts = posts.order_by('-inquiry','-pub_date')
        elif so ==  'scrap':
            posts = posts.order_by('-scrap','-pub_date')
        else:
            posts = posts.order_by('-pub_date')
        
        #페이지 나누기 추후 추가
        #paginator = Paginator(content_list,5)
        #page = request.GET.get('page','')
        #posts = paginator.get_page(page)
        
        return render(request,'main/mainlistpage.html',{'posts':posts, 'kw': kw, 'so': so})
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
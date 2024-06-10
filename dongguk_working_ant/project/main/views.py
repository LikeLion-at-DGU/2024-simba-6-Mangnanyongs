from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Post

# Create your views here.
def mainpage(request):
    posts = Post.objects.all()
    return render(request, 'main/mainpage.html', {'posts':posts})

def mainlistpage(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()

        sort = request.GET.get('sort','')
        if sort == 'deadline':
            posts = Post.objects.all().order_by('-deadline','-pub_date')
        elif sort ==  'inquiry':
            posts = Post.objects.all().order_by('-inquiry','-pub_date')
        elif sort ==  'scrap':
            posts = Post.objects.all().order_by('-scrap','-pub_date')
        else:
            posts = Post.objects.all().order_by('-pub_date')
            
        #페이지 나누기 추후 추가
        #paginator = Paginator(content_list,5)
        #page = request.GET.get('page','')
        #posts = paginator.get_page(page)
        
        return render(request,'main/mainlistpage.html',{'posts':posts,'sort':sort})
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
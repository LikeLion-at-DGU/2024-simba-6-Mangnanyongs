from django.shortcuts import render,redirect

# Create your views here.
def staff_mypage(request):
    return render(request, 'users/staff_mypage.html')
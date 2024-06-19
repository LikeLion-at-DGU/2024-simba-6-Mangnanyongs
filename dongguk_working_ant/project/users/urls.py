from django.urls import path
from .views import *
# from users import views #추가한코드

app_name = "users"
urlpatterns = [
    path('staff-mypage/', staff_mypage, name="staff-mypage"),
    path('staff-appslist/', staff_appslist, name="staff_appslist"),
    path('staff-mypost/', staff_mypost, name="staff_mypost"),
    path('staff-studentappfile/', staff_studentappfile, name="staff_studentappfile"),
    path('student-myapplication/', student_myapplication, name="student_myapplication"),
    path('student-mypage/', student_mypage, name="student-mypage"),
    path('student-myscrap/', student_myscrap, name="student_myscrap"),
    path('student-mywork/', student_mywork, name="student_mywork"),
]

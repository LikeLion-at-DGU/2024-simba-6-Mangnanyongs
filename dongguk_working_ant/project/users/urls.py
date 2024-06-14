from django.urls import path
from .views import *
# from users import views #추가한코드

app_name = "users"
urlpatterns = [
    path('staff-mypage/', staff_mypage, name="staff-mypage"),
]

from django.urls import path
from .views import *

app_name = "accounts"
urlpatterns = [
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('signup-choose/', signup_choose, name="signup-choose"),
    path('signup-student/', signup_student, name="signup-student"),
    path('signup-staff/', signup_staff, name="signup-staff"),
    path('delete-account/', delete_account, name="delete-account"),
]
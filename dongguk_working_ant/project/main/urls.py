from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', mainpage, name="mainpage"),
    path('mainlistpage/', mainlistpage, name="mainlistpage"),
    path('post-edit/', post_edit, name="post-edit"),
    #이동건 수정한부분 
    path('workDetailPage/<int:post_id>/', workDetailPage, name="workDetailPage")
]

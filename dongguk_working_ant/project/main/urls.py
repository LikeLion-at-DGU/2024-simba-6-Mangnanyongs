from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', mainpage, name="mainpage"),
    path('mainlistpage/', mainlistpage, name="mainlistpage"),
    path('post-edit/', post_edit, name="post-edit"),
    path('post-detail/<int:id>', post_detail, name="post-detail")
]

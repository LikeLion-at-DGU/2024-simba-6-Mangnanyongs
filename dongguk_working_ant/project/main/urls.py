from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', mainpage, name="mainpage"),
    path('mainlistpage/', mainlistpage, name="mainlistpage"),
    path('new-post', new_post, name="new-post"),
    path('post-edit/<int:id>', post_edit, name="post-edit"),
    path('post-create/', post_create, name="post-create"),
    path('post-detail/<int:post_id>', post_detail, name="post-detail"),
    path('scrap/<int:post_id>', scraps, name="scraps"),
    path('apply/', apply, name="apply"),
    path('post_edit_modal/', post_edit_modal, name="post-edit-modal"),
    path('update/<int:id>', post_update, name="post-update"),
]

from django.urls import path
from todolist.views import show_list
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import create_task
from todolist.views import delete_task
from todolist.views import update_task

app_name = 'todolist'

urlpatterns = [
    path('', show_list, name='show_list'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'), 
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create-task'),
    path('delete-task/<int:post_id>', delete_task, name='delete-task'),
    path('update-task/<int:post_id>', update_task, name='update-task'),
]

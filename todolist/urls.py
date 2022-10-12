from django.urls import path
from todolist.views import delete_task_json, show_list
from todolist.views import register, login_user, logout_user
from todolist.views import create_task, delete_task, update_task
from todolist.views import add_task_json, show_list_json, delete_task_json

app_name = 'todolist'

urlpatterns = [
    path('', show_list, name='show_list'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'), 
    path('logout/', logout_user, name='logout'),
    path('create/', create_task, name='create-task'),
    path('delete/<int:post_id>', delete_task, name='delete-task'),
    path('update/<int:post_id>', update_task, name='update-task'),
    path('delete/json/<int:post_id>', delete_task_json, name='delete_task_json'),
    path('json', show_list_json, name='show_list_json'),
    path('create/json', add_task_json),
]

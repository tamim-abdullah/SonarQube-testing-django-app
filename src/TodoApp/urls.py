from django.urls import path
from views.auth_view import login_user, logout_user, register_user
from views.tasks_view import index, update_task, delete_task

urlpatterns = [
    path('', index, name='list'),
    path('update_task/<str:pk>/', update_task, name='update_task'),
    path('delete/<str:pk>/', delete_task, name='delete'),
    path('register/', register_user, name='register'), 
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]

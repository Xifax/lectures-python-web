from django.urls import path

from . import views


app_name = 'tasks'
urlpatterns = [
    path('', views.landing, name='landing'),

    path('answers', views.AnswerList.as_view(), name='answer-list'),
    path('answers/<int:pk>', views.AnswerDetails.as_view(), name='answer-view'),

    path('tasks', views.my_tasks, name='task-list'),
    path('tasks/<int:pk>', views.view_task, name='task-view'),

    path('accounts/profile/', views.profile, name='profile')
]



from django.urls import path
from .views import task_create, logik, list_tasks

app_name = 'questions'

urlpatterns = [
    path('', task_create, name='add_task'),
    path('logik/', logik, name="logika"),
    path('list/', list_tasks, name='list')
]

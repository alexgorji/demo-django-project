from django.urls import path
from .views import TaskCreateView, TaskListView, TaskUpdateView, TaskDeleteView

app_name = 'tasks'

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('new', TaskCreateView.as_view(), name='task-create'),
    path("<int:pk>/update", TaskUpdateView.as_view(), name='task-update'),
    path("<int:pk>/delete", TaskDeleteView.as_view(), name='task-delete')
]

from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.shortcuts import reverse
from tasks.models import Task


class TaskCreateView(CreateView):
    model = Task
    fields = ['text']

    def get_success_url(self):
        return reverse('tasks:task-list')


class TaskListView(ListView):
    model = Task


class TaskUpdateView(UpdateView):
    model = Task
    fields = ['text']


class TaskDeleteView(DeleteView):
    model = Task

    def get_success_url(self):
        return reverse('tasks:task-list')

from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task
from .forms import TaskForm
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404


class AddTaskView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)


class ToggleTaskStatusView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, author=request.user)
        task.status = not task.status
        task.save()

        return JsonResponse({"status": task.status})


class EditTaskView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo/task_edit.html'
    success_url = reverse_lazy("home")

    def get(self, *args, **kwargs):
        return HttpResponseRedirect(self.success_url)
    
    def form_invalid(self, form):
        return HttpResponseRedirect(self.success_url)

class DeleteTaskView(DeleteView):
    model = Task
    success_url = reverse_lazy("home")

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)

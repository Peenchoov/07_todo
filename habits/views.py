from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Habit
from .forms import HabitForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404
from datetime import date


class AddHabitView(CreateView):
    model = Habit
    form_class = HabitForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)


class ToggleHabitStatusView(View):
    def post(self, request, pk):
        habit = get_object_or_404(Habit, pk=pk, author=request.user)
        habit.status = not habit.status
        if habit.status:
            habit.last_completed = date.today()
        habit.save()
        return JsonResponse({"status": habit.status})


class EditHabitView(UpdateView):
    model = Habit
    form_class = HabitForm
    template_name = "todo/habit_edit.html"
    success_url = reverse_lazy("home")

    def get(self, *args, **kwargs):
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        return HttpResponseRedirect(self.success_url)


class DeleteHabitView(DeleteView):
    model = Habit
    success_url = reverse_lazy("home")

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)

from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from todo.models import Task
from habits.models import Habit
from notes.models import Note
from datetime import date, timedelta


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            context["tasks"] = Task.objects.filter(author=self.request.user)
            user_habits = Habit.objects.filter(author=self.request.user)
            today = date.today()

            for habit in user_habits:
                if habit.last_completed:
                    should_reset = False

                    days_since_completed = (today - habit.last_completed).days

                    if habit.interval_type == "DAILY" and days_since_completed >= 1:
                        should_reset = True
                    elif habit.interval_type == "WEEKLY" and days_since_completed >= 7:
                        should_reset = True
                    elif (
                        habit.interval_type == "MONTHLY" and days_since_completed >= 30
                    ):
                        should_reset = True
                    elif (
                        habit.interval_type == "WEEKDAYS"
                        and today.weekday() < 5
                        and days_since_completed >= 1
                    ):
                        should_reset = True
                    elif (
                        habit.interval_type == "WEEKENDS"
                        and today.weekday() >= 5
                        and days_since_completed >= 1
                    ):
                        should_reset = True
                    elif (
                        habit.interval_type == "CUSTOM_DAYS"
                        and days_since_completed >= habit.interval_days
                    ):
                        should_reset = True

            context["habits"] = user_habits

            expired_notes = Note.objects.filter(
                author=self.request.user, time_to_delete__lte=today
            )
            expired_notes.delete()

            user_notes = Note.objects.filter(author=self.request.user)

            can_add_note = user_notes.count() < 5
            context["notes"] = user_notes
            context["can_add_note"] = can_add_note
        return context


class WhatsNewPageView(TemplateView):
    template_name = "whatsnew.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


class ContactPageView(TemplateView):
    template_name = "contact.html"

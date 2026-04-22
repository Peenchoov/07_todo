from django.urls import path
from .views import AddHabitView, DeleteHabitView, EditHabitView, ToggleHabitStatusView

urlpatterns = [
    path("add_habit", AddHabitView.as_view(), name="add_habit"),
    path(
        "habit/<int:pk>/toggle/", ToggleHabitStatusView.as_view(), name="toggle_habit"
    ),
    path("habit/<int:pk>/delete/", DeleteHabitView.as_view(), name="delete_habit"),
    path("habit/<int:pk>/edit/", EditHabitView.as_view(), name="edit_habit"),
]

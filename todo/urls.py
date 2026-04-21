from django.urls import path
from .views import AddTaskView, DeleteTaskView, EditTaskView, ToggleTaskStatusView

urlpatterns = [
    path("add_task", AddTaskView.as_view(), name="add_task"),
    path("task/<int:pk>/toggle/", ToggleTaskStatusView.as_view(), name="toggle_task"),
    path("task/<int:pk>/delete/", DeleteTaskView.as_view(), name="delete_task"),
    path("task/<int:pk>/edit/", EditTaskView.as_view(), name="edit_task"),
]

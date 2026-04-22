from django.urls import path
from .views import AddNoteView, EditNoteView, DeleteNoteView

urlpatterns = [
    path("add_note", AddNoteView.as_view(), name="add_note"),
    path("note/<int:pk>/delete/", DeleteNoteView.as_view(), name="delete_note"),
    path("note/<int:pk>/edit/", EditNoteView.as_view(), name="edit_note"),
]

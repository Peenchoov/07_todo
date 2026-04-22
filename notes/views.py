from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Note
from .forms import NoteForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


class AddNoteView(CreateView):
    model = Note
    form_class = NoteForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        if Note.objects.filter(author=self.request.user).count() >= 5:
            return HttpResponseRedirect(self.success_url)

        form.instance.author = self.request.user
        return super().form_valid(form)


class EditNoteView(UpdateView):
    model = Note
    form_class = NoteForm
    success_url = reverse_lazy("home")

    def get(self, *args, **kwargs):
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        return HttpResponseRedirect(self.success_url)


class DeleteNoteView(DeleteView):
    model = Note
    success_url = reverse_lazy("home")

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)

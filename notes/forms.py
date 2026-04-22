from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = (
            "content",
            "category",
            "date_in_note",
            "time_to_delete",
        )

from django.contrib import admin
from .models import Note

# Register your models here.


class NoteAdmin(admin.ModelAdmin):
    list_display = (
        "content",
        "category",
        "date_in_note",
        "author",
        "time_to_delete",
        "date_added",
    )


admin.site.register(Note, NoteAdmin)

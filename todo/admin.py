from django.contrib import admin
from .models import Task

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "status",
        "deadline",
        "category",
        "overdue",
        "date_added",
        "last_modified",
        "author",
    )


admin.site.register(Task, TaskAdmin)

from django.contrib import admin
from .models import Habit

# Register your models here.


class HabitAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "status",
        "category",
        "number_of_repetitions",
        "current_streak",
        "best_streak",
        "date_added",
        "last_completed",
        "author",
        "interval_type",
    )


admin.site.register(Habit, HabitAdmin)

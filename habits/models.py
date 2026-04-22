from django.db import models
from django.conf import settings


class Habit(models.Model):
    name = models.TextField(max_length=100)
    status = models.BooleanField(default=False)
    category = models.TextField(max_length=100, blank=True, null=True)
    number_of_repetitions = models.PositiveIntegerField(default=1)
    current_streak = models.PositiveIntegerField(default=0)
    best_streak = models.PositiveIntegerField(default=0)
    date_added = models.DateField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    last_completed = models.DateField(null=True, blank=True)
    INTERVAL_CHOICES = [
        ("DAILY", "Daily"),
        ("WEEKLY", "Weekly"),
        ("MONTHLY", "Monthly"),
        ("WEEKDAYS", "Weekdays"),
        ("WEEKENDS", "Weekends"),
        ("CUSTOM_DAYS", "Custom Days"),
    ]
    interval_type = models.CharField(
        max_length=20, choices=INTERVAL_CHOICES, default="DAILY"
    )

    interval_days = models.PositiveIntegerField(default=1, null=True, blank=True)

    def __str__(self):
        return self.name

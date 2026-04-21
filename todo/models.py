from django.db import models
from django.conf import settings

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    deadline = models.DateField()
    category = models.TextField(max_length=100)
    overdue = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

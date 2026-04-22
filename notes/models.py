from django.db import models
from django.conf import settings

# Create your models here.


class Note(models.Model):
    content = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True, null=True)
    date_in_note = models.DateField(null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_to_delete = models.DateField(null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.content

from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=250)
    completed = models.BooleanField(default=True, null=True, blank=True)

    def __str__(self):
        return self.title
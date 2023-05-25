from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    date = models.DateField(blank=False)
    isdone = models.DateField(default=False)

    def __str__(self) -> str:
        return self.title

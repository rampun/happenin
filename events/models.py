from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name
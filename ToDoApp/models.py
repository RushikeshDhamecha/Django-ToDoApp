from django.db import models


# Create your models here.
class Task(models.Model):
    addTitle = models.CharField(max_length=30)
    addDesc = models.TextField(max_length=1000)

    def __str__(self):    # This shows name of title in database
        return self.addTitle

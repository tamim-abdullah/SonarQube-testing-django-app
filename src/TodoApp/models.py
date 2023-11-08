from django.db import models

class Todo(models.Model):
    task = models.CharField(max_length = 50)
    description = models.CharField(max_length = 100)
from django.db import models

class Todo(models.Model):
<<<<<<< HEAD
    task = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
=======
    task = models.CharField(max_length = 50)
    description = models.CharField(max_length = 100 , null=True , blank=True) 
    is_completed = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.task
>>>>>>> 0b5ceb8399d39639d93253c2d4b7799c7c06c851

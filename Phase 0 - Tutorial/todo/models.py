from django.db import models

# Create your models here.
from django.db import models

class Todo(models.Model):
    done = models.BooleanField(default=False)
    description = models.TextField()
    

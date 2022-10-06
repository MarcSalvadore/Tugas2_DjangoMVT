from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class toDo(models.Model):
    is_finished = models.BooleanField(default=False)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.TextField()
    title = models.TextField()
    description = models.TextField()
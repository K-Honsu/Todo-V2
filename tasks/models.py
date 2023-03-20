from django.db import models
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
User = get_user_model()

# Create your models here.


class Tasks(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

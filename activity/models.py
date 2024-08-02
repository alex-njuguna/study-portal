from django.db import models
from django.contrib.auth.models import User


"""
Activity model with fields:
1. user
2. title
3. is_finished
"""
class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        """
        return the titile of the activity
        """
        return self.title


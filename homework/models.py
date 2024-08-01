from django.db import models
from django.contrib.auth.models import User


"""
user - homework author
subject - the subject
title - homework title
some description
due date
is_finished - true or false
"""
class Homework(models.Model):
    user = models .ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due = models.DateTimeField()
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        """
        get homework titile
        """
        return self.title

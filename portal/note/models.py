from django.db import models
from django.contrib.auth.models import User


# notes table
class Note(models.Model):
    """
    user - author
    title - note title
    description - note description
    created_at - date created
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        get the note title and date created
        """
        return f"{self.title} - {self.created_at}" 
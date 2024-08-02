from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User


"""model to hold books saved by the user"""
class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    contents = models.FileField(upload_to="books/", validators=[FileExtensionValidator(["pdf", "epub"])])

    def __str__(self):
        """show book title"""
        return self.title


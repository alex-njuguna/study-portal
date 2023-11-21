from django.db import models
from django.core.validators import FileExtensionValidator


"""model to hold books saved by the user"""
class Book(models.Model):
    title = models.CharField(max_length=50)
    contents = models.FileField(upload_to="books/", validators=[FileExtensionValidator(["pdf", "epub"])])

    def __str__(self):
        """show book title"""
        return self.title


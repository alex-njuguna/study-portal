from django import forms

from .models import Activity


"""
model form to create an activity
fields - title
"""
class ActivityForm(forms.ModelForm):
    """define the model, fields, labels and widgets"""
    class Meta:
        model = Activity
        fields = ["title"]
        labels = {
            "title": "Title: "
        }

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control"
            })
        }
from django import forms

from .models import Activity


"""
model form to create an activity
fields - title
"""
class ActivityForm(forms.ModelForm):
    """define the model, fields, labels and widgets"""
    title = forms.CharField(max_length=200, label="", required=True, widget=forms.widgets.TextInput(attrs={"class": "form-control", "placeholder" : "Activity Title"}))
    class Meta:
        model = Activity
        fields = ["title"]
        
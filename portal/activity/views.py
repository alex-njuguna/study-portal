from django.shortcuts import render, redirect

from .models import Activity
from .forms import ActivityForm


def home(request):
    """
    display all activities(title, status, delete action)
    show an add activity form
    """
    activities = Activity.objects.filter(user=request.user)

    return render(request, "activity/home.html", {
        "title": "activities",
        "activities": activities
    })

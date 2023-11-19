from django.shortcuts import render, redirect
from django.contrib import messages

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


def update_activity(request, id):
    """
    update the status of the activity from either
    is_finished or not and vice-versa
    """
    activity = Activity.objects.get(user=request.user, id=id)

    if activity.is_finished == False:
        activity.is_finished = True
        activity.save()
        messages.info(request, f"Status for activity '{activity.title.upper()}' updated")
    else:
        activity.is_finished = False
        activity.save()
        messages.info(request, f"Status for activity '{activity.title.upper()}' updated")
    return redirect("activity:home")

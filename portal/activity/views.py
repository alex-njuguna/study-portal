from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Activity
from .forms import ActivityForm


def home(request):
    """
    display all activities(title, status, delete action)
    show an add activity form
    """
    if request.method == "POST":
        form = ActivityForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data.get("title")
            
            activity = Activity(user=request.user, title=title)
            activity.save()
            messages.success(request, f"Activity '{title.upper()}' added.")

            return redirect("activity:home")

    else:
        form = ActivityForm()

    activities = Activity.objects.filter(user=request.user)

    return render(request, "activity/home.html", {
        "title": "activities",
        "activities": activities,
        "form": form
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


def delete_activity(request, id):
    """delete a given activity"""
    activity = Activity.objects.get(user=request.user, id=id)

    title = activity.title
    activity.delete()
    messages.info(request, f"Activity '{title.upper()}' deleted")

    return redirect("activity:home")
    
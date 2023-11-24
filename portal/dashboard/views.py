from django.shortcuts import render

from activity.models import Activity
from homework.models import Homework


def home(request):

    return render(request, "dashboard/home.html", {"title": "dashboard"})


def profile(request):
    """
    return undone activities
    return undone homeworks
    """
    activities = Activity.objects.filter(user=request.user, is_finished=False)

    return render(request, "dashboard/profile.html", {
        "activities": activities
    })

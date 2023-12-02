from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from activity.models import Activity
from homework.models import Homework


def home(request):

    return render(request, "dashboard/home.html", {"title": "dashboard"})

@login_required
def profile(request):
    """
    return undone activities
    return undone homeworks
    """
    activities = Activity.objects.filter(user=request.user, is_finished=False)
    homeworks = Homework.objects.filter(user=request.user, is_finished=False)

    return render(request, "dashboard/profile.html", {
        "activities": activities,
        "homeworks": homeworks,
        "title": "profile"
    })

@login_required
def signout(request):
    """
    logout the current user
    """
    logout(request)

    return redirect("dashboard:home")

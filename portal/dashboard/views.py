from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from activity.models import Activity
from homework.models import Homework


def home(request):

    return render(request, "dashboard/home.html", {"title": "dashboard"})

def login_user(request):
    if request.method == "POST":
        data = request.POST
        username = data["username"]
        password = data["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Logged in...")
        else:
            messages.warning(request, "Invalid details...")
            return redirect(request.path)
    
    return render(request, "dashboard/login.html")

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

from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from activity.models import Activity
from homework.models import Homework

from .forms import RegisterUserForm, ChangeUserForm


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
            return redirect("dashboard:home")
            
        else:
            messages.warning(request, "Invalid details...")
            return redirect(request.path)
    
    return render(request, "dashboard/login.html", {"title": "login"})

def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard:home")
    form = RegisterUserForm()
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            username = data["username"]
            password = data["password1"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, "User created and logged in...")
                return redirect("dashboard:home")
        else:
            for error in list(form.errors.value()):
                messages.warning(request, error)
            return redirect(request.path)
    
    context = {
        "title": "register",
        "form": form,
    }
    
    return render(request, "dashboard/register.html", context)

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

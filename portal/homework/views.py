from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Homework


def home(request):
    """
    get all homeworks for a specific user
    display a form to add a homework
    """
    homeworks = Homework.objects.filter(user=request.user)

    return render(request, "homework/home.html", {
        "title": "homework",
        "homeworks": homeworks
    })

def update_homework(request, id):
    """
    update homework to either complete or not
    """
    homework = Homework.objects.get(user=request.user, id=id)

    if homework.is_finished == True:
        homework.is_finished = False
        messages.info(request, f"{homework.title} marked as NOT finished")
        homework.save()
    else:
        homework.is_finished = True
        messages.success(request, f"{homework.title} marked as FINISHED")
        homework.save()
    
    return redirect("homework:home")







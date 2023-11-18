from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Homework
from.forms import AddHomeworkForm


def home(request):
    """
    get all homeworks for a specific user
    display a form to add a homework
    """
    if request.method == "POST":
        form = AddHomeworkForm(request.POST)

        if form.is_valid():
            user = request.user
            subject = form.cleaned_data.get("subject")
            title = form.cleaned_data.get("title")
            description = form.cleaned_data.get("description")
            due = form.cleaned_data.get("due")
            finished = form.cleaned_data.get("is_finished")

            try:
                if finished == "on":
                    finished = True
                else:
                    finished = False
            except:
                finished = False

            homework = Homework(user=user, subject=subject, title=title,
                                description=description, due=due, finished=finished)
            homework.save()

            messages.success(request, f"Homework: {title} added successfully")

            return redirect("homework:home")
    else:
        form = AddHomeworkForm()

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


def delete_homework(request, id):
    """
    delete a given homework
    """
    homework = Homework.objects.get(user=request.user, id=id)

    title = homework.title
    homework.delete()
    messages.warning(request, f"{title} homework deleted!")

    return redirect("homework:home")




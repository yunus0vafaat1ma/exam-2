from django.shortcuts import render, HttpResponse, redirect
from .forms import QuestionForm
from .models import Question


def task_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'save.html')
        else:
            return HttpResponse("Form is invalid")
    form = {'form': QuestionForm}
    return render(request, 'list.html', form)


def logik(request):
    return render(request, 'save.html')


def list_tasks(request):
    questions = Question.objects.all()
    return render(request, 'lists.html', {'questions': questions })
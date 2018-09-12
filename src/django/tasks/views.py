from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Answer, Task


def landing(request):
    return render(request, 'landing.html')


@login_required
def profile(request):
    return render(request, 'profile.html')


@method_decorator(login_required, name='dispatch')
class AnswerList(generic.ListView):
    model = Answer
    template_name = 'teachers/answer_list.html'
    context_object_name = 'answer_list'

    def get_queryset(self):
        return Answer.objects.all()


class AnswerDetails(generic.DetailView):
    model = Answer
    template_name = 'teachers/answer.html'


@login_required
def my_tasks(request):
    if not hasattr(request.user, 'student'):
        raise PermissionDenied
    return render(request, 'students/task_list.html')


def view_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'students/task.html', {
        'task': task
    })

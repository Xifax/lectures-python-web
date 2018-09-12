from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import AnswerForm
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

    def dispatch(self, request, *args, **kwargs):
        if hasattr(request.user, 'student'):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


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
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            # NB: will create a new answer each time!
            answer = form.save(commit=False)
            answer.student = request.user.student
            answer.task = task
            answer.save()
            return redirect(reverse('tasks:task-view', kwargs={'pk': task.pk}))
    else:
        form = AnswerForm()

    try:
        answer = Answer.objects.filter(task=task, student=request.user.student).last()
    except Answer.DoesNotExist:
        pass

    return render(request, 'students/task.html', {
        'task': task,
        'form': form,
        'answer': answer
    })

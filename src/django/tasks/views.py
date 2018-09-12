from django.shortcuts import render
from django.views import generic

from .models import Answer


def landing(request):
    return render(request, 'landing.html')


class AnswerList(generic.ListView):
    model = Answer
    template_name = 'teachers/answer_list.html'
    context_object_name = 'answer_list'

    def get_queryset(self):
        return Answer.objects.all()


class AnswerDetails(generic.DetailView):
    model = Answer
    template_name = 'teachers/answer.html'

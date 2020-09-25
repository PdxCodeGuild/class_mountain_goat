from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice

def index(request):
    questions = Question.objects.all()
    # for question in questions:
    #     print(question.question_text)
    context = {
        'questions': questions
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # return HttpResponse(f"Detail page for question with id {question_id}.")
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, id=question_id)
    context = {
        'question': question
    }
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    context = {
        'question': question
    }
    return render(request, 'polls/results.html', context)

def vote(request, question_id):
    choice = Choice.objects.get(id=request.POST['choice_id'])
    choice.votes += 1
    choice.save()
    # print(request.POST)
    return HttpResponseRedirect(reverse('polls:results', args=[question_id]))
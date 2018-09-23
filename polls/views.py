# -*- coding:utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.urls import reverse
from django.template import loader
from django.http import Http404


def index(request):
    return HttpResponse('hello world you are at polls index')


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    # try:
    #     question = Question.objects.get(pk=question_id)
    #     context = {'question': question}
    # except Exception as e:
    #     print(e)
    #     raise Http404("id = %s Question does not exist" % str(question_id))
    # return HttpResponse("You're looking at question %s." % question_id)

    return render(request, 'polls/detail.html', context=context)


def order(request):
    """问题排序，取最近五个"""
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context=context)  # 等价于下面两句

    # tempalte = loader.get_template('polls/index.html')
    # return HttpResponse(tempalte.render(context, request))


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        select_choice = question.choice_set.get(pk=request.POST['choice'])
    except Exception as e:
        print('polls/vote exception= ', e)
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    select_choice.votes += 1
    select_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})





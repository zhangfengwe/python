
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from .models import Question

from datetime import datetime

from python.study.other.config.logger import Logger

# Create your views here.
logger = Logger().get_logger()


# 通用模板,只需要设置相关数据信息,无需编写逻辑代码
class IndexView(generic.ListView):
    template_name = 'app1/all.html'
    context_object_name = 'question_list'
    model = Question


class DetailView(generic.DetailView):
    template_name = 'app1/detail.html'
    model = Question


def index(request):
    logger.info('app1 index')
    question_list = Question.objects.all()
    return render(request, 'app1/all.html', {'question_list': question_list, 'year': datetime.now().year})


def detail(request, question_id):
    logger.info('app1 detail {}'.format(question_id))
    question = Question.objects.get(id=question_id)
    return HttpResponse(question)


def add(request):
    question = Question(question_text=request.POST['question_text'], pub_date=request.POST['pub_date'])
    question.save()
    return HttpResponseRedirect(reverse('app1:index'))


def showadd(request):
    return render(request, 'app1/add.html')

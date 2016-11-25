from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .modelmanager import ModelManager
from Ask_buk.models import Question, Answer, Tag
import random

# Create your views here.

def paginate(objects_list, request):
	page = request.GET.get('page')

	p = Paginator(objects_list, 10)
	try:
		object_page = p.page(page)
	except PageNotAnInteger:
		object_page = p.page(1)
	except EmptyPage:
		object_page = p.page(1)
	return object_page

def index(request):
	posts=Question.objects.new_questions()
	pagination = paginate(posts, request)
	return render(request, 'index.html', {'posts': pagination})

def hot(request, page=1):
	posts=Question.objects.hot_questions()
	pagination = paginate(posts, request)
	return render(request, 'hot.html', {'posts': pagination})

def questions_tag(request, tag):
	questions_tag=Question.objects.questions_by_tag(tag)	
	pagination = paginate(questions_tag, request)
	return render(request, 'questions.html', {'posts': pagination, 'tag': tag})

def question(request):
    return render(request, 'question.html', {})

def settings(request):
    return render(request, 'settings.html', {})

def ask(request, id_quest):
	question=get_object_or_404(Question, id=id_quest)
	posts = Answer.objects.filter(question=question)
	pagination = paginate(posts, request)
	return render(request, 'ask.html', {'answer': pagination, 'post': question})

def login(request):
    return render(request, 'login.html', {})

def signup(request):
    return render(request, 'signup.html', {})

# Create your views here.

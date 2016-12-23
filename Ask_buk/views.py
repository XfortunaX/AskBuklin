from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserSignupForm, ProfileSignupForm, AnswerForm, QuestionForm, UserForm
from django.contrib.auth import login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .modelmanager import ModelManager
from Ask_buk.models import Question, Answer, Tag, Like_Question, User, Like_Answer
from django.http import JsonResponse
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
	return render(request, 'questions_tag.html', {'posts': pagination, 'tag': tag})

def ask(request):
	if request.method == 'POST':
		form = QuestionForm(request.POST)
		if form.is_valid():
			question = form.save(commit=False)
			question.author = request.user
			question.like_count = 0
			question.save()
			return HttpResponseRedirect('/')
	else:
		form = QuestionForm()
	return render(request, 'ask.html', {'form':form})

def question(request, id_quest):
	question=get_object_or_404(Question, id=id_quest)
	posts = Answer.objects.filter(question=question)
	pagination = paginate(posts, request)
	if request.method == 'POST':
		form = AnswerForm(request.POST)
		if form.is_valid():
			answer = form.save(commit=False)
			answer.title = question.title
			answer.author = request.user
			answer.question = question
			answer.like_count = 0
			answer.save()
			question.answer_count += 1
			question.save()
			return HttpResponseRedirect('/question/' + id_quest)
	else:
		form = AnswerForm()
	return render(request, 'question.html', {'answers': pagination, 'post': question, 'form': form})

def log_in(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			if form.get_user():
				user = form.get_user()
				login(request, user)
				return HttpResponseRedirect('/')
	else:
		form = LoginForm()
	return render(request, 'log_in.html', {'form': form})

@login_required
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')

def signup(request):
	if request.method == 'POST':
		userForm = UserSignupForm(request.POST,  prefix="userForm")
		profileForm = ProfileSignupForm(request.POST, request.FILES,  prefix="profileForm")
		if userForm.is_valid() and profileForm.is_valid():
			user = userForm.save()
			profile = profileForm.save(commit=False)
			profile.user = user
			profile.save()
			return HttpResponseRedirect('/')
	else:
		userForm = UserSignupForm(prefix="userForm")
		profileForm = ProfileSignupForm(prefix="profileForm")
	return render(request, 'signup.html', {'userForm': userForm, 'profileForm': profileForm})

def settings(request):
	if request.method == 'POST':
		userForm = UserForm(request.POST, instance=request.user, prefix="userForm")
		profileForm = ProfileSignupForm(request.POST, request.FILES,  prefix="profileForm", instance=request.user.profile)
		if userForm.is_valid() and profileForm.is_valid():
			userForm.save()
			profileForm.save()
			return HttpResponseRedirect('/')
	else:
		userForm = UserForm(prefix="userForm", instance=request.user)
		profileForm = ProfileSignupForm(prefix="profileForm", instance=request.user.profile)
	return render(request, 'settings.html', {'userForm': userForm, 'profileForm': profileForm})

@login_required
def like_q(request):
	if request.method == 'POST':
		try:
			question = Question.objects.get(pk=request.POST.get('id', 0))
			user = User.objects.get(pk=request.POST.get('id_user', 0))
			like_quest = Like_Question.objects.get(user=user, question=question, is_like=True)
		except Like_Question.DoesNotExist:
			like_quest_new = Like_Question(user=user, question=question, is_like=True)
			like_quest_new.save()
			question.like_count += 1
			question.save()
			return JsonResponse({ "status": "ok" })
	return JsonResponse({ "status": "error" })

@login_required
def like_a(request):
	if request.method == 'POST':
		try:
			answer = Answer.objects.get(pk=request.POST.get('id', 0))
			user = User.objects.get(pk=request.POST.get('id_user', 0))
			like_answer = Like_Answer.objects.get(user=user, answer=answer, is_like=True)
		except Like_Answer.DoesNotExist:
			like_answer_new = Like_Answer(user=user, answer=answer, is_like=True)
			like_answer_new.save()
			answer.like_count += 1
			answer.save()
			return JsonResponse({ "status": "ok" })
	return JsonResponse({ "status": "error" })

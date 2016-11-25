from __future__ import unicode_literals

from django.contrib.auth.models import User 
from django.db import models
from .modelmanager import ModelManager

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	nickname = models.CharField('Nickname', max_length=30)
	avatar = models.ImageField('Avatar', upload_to='avatars/')

	def __str__(self):
		return 'User {1}'.format(self.user.username)

class Tag(models.Model):
    name = models.CharField('Tag', unique=True, max_length=16)

    def __str__(self):
        return self.name

class Question(models.Model):
	title = models.CharField('Title', max_length=255)
	content = models.TextField('Text')
	author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
	tags = models.ManyToManyField('Tag')
    
	created_date = models.DateTimeField('Creation date', auto_now=True)
	like_count = models.IntegerField('Like count')
	dislike_count = models.IntegerField('Dislike count')

	objects = ModelManager()

	def __str__(self):
		return self.title

class Answer(models.Model):
	title = models.CharField('Title', max_length=255)
	content = models.TextField('Text')
	author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
	question = models.ForeignKey(Question)
    
	created_date = models.DateTimeField('Creation date', auto_now=True)
	like_count = models.IntegerField('Like count')
	dislike_count = models.IntegerField('Dislike count')

	def __str__(self):
		return self.title

class Like_question(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	question = models.ForeignKey(Question)  

	def __str__(self):
		return 'User {1} liked {2}'.format(self.user.profile.nickname, self.question.title)

class Like_answer(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	answer = models.ForeignKey(Answer)  

	def __str__(self):
		return 'User {1} liked {2}'.format(self.user.profile.nickname, self.answer.title)

from __future__ import unicode_literals

from django.contrib.auth.models import User 
from django.db import models
from .modelmanager import ModelManager

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	nickname = models.CharField('Nickname', max_length=30)
	avatar = models.ImageField('Avatar', upload_to='uploads/')

	def __str__(self):
		return 'User {}'.format(self.user.username)

	class Meta:
		verbose_name = 'Profile'
		verbose_name_plural = 'Profiles'

class Tag(models.Model):
    name = models.CharField('Tag', unique=True, max_length=16)

    def __str__(self):
        return self.name

	class Meta:
		verbose_name = 'Tag'
		verbose_name_plural = 'Tags'

class Question(models.Model):
	title = models.CharField('Title', max_length=255)
	content = models.TextField('Text')
	author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
	tags = models.ManyToManyField('Tag')
    
	created_date = models.DateTimeField('Creation date', auto_now=True)
	like_count = models.IntegerField('Like count', default=0)
	answer_count = models.IntegerField('Answer count', default=0)

	objects = ModelManager()

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Question'
		verbose_name_plural = 'Questions'

class Answer(models.Model):
	title = models.CharField('Title', max_length=255)
	content = models.TextField('Text')
	author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
	question = models.ForeignKey(Question)
    
	created_date = models.DateTimeField('Creation date', auto_now=True)
	like_count = models.IntegerField('Like count', default=0)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Answer'
		verbose_name_plural = 'Answers'

class Like_Question(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	question = models.ForeignKey(Question)
	is_like = models.BooleanField(default=True)	

	def __str__(self):
		return 'User {} like {} '.format(self.user.profile.nickname, self.question)

	class Meta:
		unique_together = ("user", "question")
		verbose_name = 'Like_question'
		verbose_name_plural = 'Likes_question'

class Like_Answer(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	answer = models.ForeignKey(Answer)
	is_like = models.BooleanField(default=True)	

	def __str__(self):
		return 'User {} like {} '.format(self.user.profile.nickname, self.answer)

	class Meta:
		unique_together = ("user", "answer")
		verbose_name = 'Like_answer'
		verbose_name_plural = 'Likes_answer'


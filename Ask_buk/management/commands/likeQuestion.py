from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from Ask_buk.models import Question, Like_question
import random

class Command(BaseCommand):
	questions = Question.objects.all()
	users = User.objects.all()

	def likeQuestions(self, max_likes):
		for question in self.questions:
			for i in range(random.randint(1, max_likes)):
				like = Like_question(user=random.choice(self.users),
					question=random.choice(self.questions))
				like.save()

	def handle(self, *args, **options):
		self.likeQuestions(max_likes=100)

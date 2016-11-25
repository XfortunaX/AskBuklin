from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from Ask_buk.models import Question, Answer
import random

class Command(BaseCommand):
	questions = Question.objects.all()
	users = User.objects.all()

	def createAnswer(self, max_ans):
		for question in self.questions:
			for i in range(random.randint(1, max_ans)):
				answer = Answer(title='Monkey D Luffi',
					content='Monkey D Luffi imba' * 7,
					author=random.choice(self.users),
					like_count=random.randint(0, 100),
					dislike_count=random.randint(0, 100),
					question=random.choice(self.questions))

				answer.save()

	def handle(self, *args, **options):
		self.createAnswer(max_ans=10)

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from Ask_buk.models import Answer, Like_answer
import random

class Command(BaseCommand):
	answers = Answer.objects.all()
	users = User.objects.all()

	def likeAnswers(self, max_likes):
		for answer in self.answers:
			for i in range(random.randint(1, max_likes)):
				like = Like_answer(user=random.choice(self.users),
					answer=random.choice(self.answers))
				like.save()

	def handle(self, *args, **options):
		self.likeAnswers(max_likes=10)

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from Ask_buk.models import Question, Like_Question
import random

class Command(BaseCommand):
	questions = Question.objects.all()
	users = User.objects.all()

	def likeQuestions(self, max_likes):
		for question in self.questions:
			for i in range(random.randint(1, max_likes)):
				like_type = random.randint(1, 100)
				if like_type < 80:
					try:
						like = Like_Question(user=random.choice(self.users),
							question=question,
							is_like=True)
						like.save()
						question.like_count += 1
						question.save()
					except:
						print('error adding like')
				else:
					try:
						like = Like_Question(user=random.choice(self.users),
							question=question,
							is_like=False)
						like.save()
						question.like_count -= 1
						question.save()
					except:
						print('error adding like')

	def handle(self, *args, **options):
		self.likeQuestions(max_likes=10)


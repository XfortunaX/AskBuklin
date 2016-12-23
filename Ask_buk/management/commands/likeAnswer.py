from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from Ask_buk.models import Answer, Like_Answer
import random

class Command(BaseCommand):
	answers = Answer.objects.all()
	users = User.objects.all()

	def likeAnswers(self, max_likes):
		for answer in self.answers:
			for i in range(random.randint(1, max_likes)):
				like_type = random.randint(1, 100)
				if like_type < 80:
					try:
						like = Like_Answer(user=random.choice(self.users),
							answer=answer,
							is_like=True)
						like.save()
						answer.like_count += 1
						answer.save()
					except:
						print('error adding like')
				else:
					try:
						like = Like_Answer(user=random.choice(self.users),
							answer=answer,
							is_like=False)
						like.save()
						answer.like_count -= 1
						answer.save()
					except:
						print('error adding like')

	def handle(self, *args, **options):
		self.likeAnswers(max_likes=10)

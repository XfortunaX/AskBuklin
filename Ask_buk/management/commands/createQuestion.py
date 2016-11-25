from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from Ask_buk.models import Question, Answer, Tag
import random

class Command(BaseCommand):
	tags = Tag.objects.all()
	users = User.objects.all()

	def createQuestions(self, n):
		for i in range(n):
			question = Question(title='Monkey D Luffi',
				content="""Monkey D. Luffy,[1] also known as "Straw Hat Luffy" and commonly as "Straw Hat",[4] is the main protagonist of the manga and anime, One Piece. He is the son of Monkey D. Dragon,[12] the grandson of Monkey D. Garp,[13] the adoptive brother of Portgas D. Ace and Sabo, and the foster son of Curly Dadan.""",
				author=random.choice(self.users),
				like_count=random.randint(0, 100),
				dislike_count=random.randint(0, 100))

			question.save()
			question.tags.add(random.choice(self.tags))
			question.save()

	def handle(self, *args, **options):
		self.createQuestions(n=7)

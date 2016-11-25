from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from Ask_buk.models import Question, Profile
import random

class Command(BaseCommand):

	def createUsers(self, n):
		for i in range(n):
			user = User(username='User {}'.format(str(random.randint(0, 100))),
                     password='pass')
			user.save()
			profile = Profile(user=user, avatar='avatars/luffi.jpg')
			profile.save()

	def handle(self, *args, **options):
		self.createUsers(n=3)

from django.db import models

class ModelManager(models.Manager):
    def new_questions(self):
        return self.order_by('created_date').reverse()

    def hot_questions(self):
        return self.order_by('like_count').reverse()

    def questions_by_tag(self, tag):
        return self.filter(tags__name=tag)



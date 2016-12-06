from django.contrib import admin
from .models import Profile
from .models import Tag
from .models import Question
from .models import Answer
from .models import Like_Question
from .models import Like_Answer

# Register your models here.

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Profile)
admin.site.register(Tag)
admin.site.register(Like_Question)
admin.site.register(Like_Answer)

# Register your models here.

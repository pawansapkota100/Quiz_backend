from django.contrib import admin
from .models import Question, Quiz, Option, UserAnswer, Result

# Register your models here.
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(UserAnswer)
admin.site.register(Result)
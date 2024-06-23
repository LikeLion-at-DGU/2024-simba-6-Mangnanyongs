from django.contrib import admin
from .models import Post, Question, Application, Answer

# Register your models here.
admin.site.register(Post)
admin.site.register(Question)
admin.site.register(Application)
admin.site.register(Answer)
from django.contrib import admin
from .models import Post, Question, Application, Answer, Review

# Register your models here.
admin.site.register(Post)
admin.site.register(Question)
admin.site.register(Application)
admin.site.register(Answer)
admin.site.register(Review)
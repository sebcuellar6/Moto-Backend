from django.contrib import admin
from .models import Profile, Messages, ForumPost, MeetUpEvent, Comment, Category

# Register your models here.
admin.site.register(Profile)
admin.site.register(Messages)
admin.site.register(ForumPost)
admin.site.register(MeetUpEvent)
admin.site.register(Comment)
admin.site.register(Category)

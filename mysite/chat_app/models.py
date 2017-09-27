from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.
class Message(models.Model):
    body = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='person_who_sends')
    date = models.DateTimeField()
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)

    def __string__(self):
        return self.title


@admin.register(Message)
class AuthorAdmin(admin.ModelAdmin):
    pass

from django.db import models

# Create your models here.
class Message(models.Model):
    body = models.TextField()
    date = models.DateTimeField()

    def __string__(self):
        return self.title

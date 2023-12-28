from django.contrib.auth.models import User
from django.db import models


class NoteModel(models.Model):
    subject = models.CharField(max_length=50)
    topic = models.CharField(max_length=250)
    description = models.TextField()
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


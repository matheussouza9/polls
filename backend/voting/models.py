from django.conf import settings
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    published_date = models.DateTimeField(auto_now_add=True)


class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="choices"
    )
    choice_text = models.CharField(max_length=200)


class Vote(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name="votes")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="votes"
    )
    timestamp = models.DateTimeField(auto_now_add=True)

from random import randint

from celery import shared_task
from django.db import transaction

from voting.models import Choice, Question


@shared_task
def create_question():
    number_of_choices = randint(2, 7)

    with transaction.atomic():
        question = Question.objects.create(question_text=f"Question {randint(1, 1000)}")
        choices = [
            Choice(choice_text=f"Choice {randint(1, 1000)}", question=question)
            for _ in range(number_of_choices)
        ]

        Choice.objects.bulk_create(choices)

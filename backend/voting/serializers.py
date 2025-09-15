from django.contrib.auth import get_user_model
from django.db import transaction

from rest_framework import serializers
from .models import Choice, Question, Vote

User = get_user_model()


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = "__all__"


class ChoiceForQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ["id", "choice_text"]


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceForQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ["id", "question_text", "published_date", "choices"]


class QuestionCreateSerializer(serializers.ModelSerializer):
    choices = serializers.ListField(
        child=serializers.CharField(max_length=255),
        required=True,
        write_only=True,
        allow_empty=False,
    )

    class Meta:
        model = Question
        exclude = ["published_date"]

    def create(self, validated_data):
        choices_data = validated_data.pop("choices")

        with transaction.atomic():
            question = Question.objects.create(**validated_data)

            Choice.objects.bulk_create(
                [
                    Choice(question=question, choice_text=choice_text)
                    for choice_text in choices_data
                ]
            )

        return question


class QuestionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["question_text"]


class VoteSerializer(serializers.ModelSerializer):
    choice = serializers.PrimaryKeyRelatedField(queryset=Choice.objects.all())

    class Meta:
        model = Vote
        fields = ["choice"]

    def validate(self, attrs):
        user = self.context["request"].user
        choice = attrs["choice"]

        if Vote.objects.filter(user=user, choice__question=choice.question).exists():
            raise serializers.ValidationError(
                "You have already voted for this question"
            )

        return attrs

    def create(self, validated_data):
        user = self.context["request"].user
        choice = validated_data["choice"]
        vote = Vote.objects.create(user=user, choice=choice)
        return vote

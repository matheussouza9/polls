from rest_framework import viewsets, permissions, status, generics
from rest_framework.response import Response


from users.permissions import IsAdminOrReadOnly

from .models import Choice, Question
from .serializers import (
    ChoiceSerializer,
    QuestionSerializer,
    QuestionCreateSerializer,
    QuestionUpdateSerializer,
    VoteSerializer,
)


class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return Question.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return QuestionCreateSerializer
        if self.action == "update":
            return QuestionUpdateSerializer

        return QuestionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        serializer_response = QuestionSerializer(instance=instance)
        return Response(serializer_response.data, status=status.HTTP_201_CREATED)


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [IsAdminOrReadOnly]


class VoteAPIView(generics.CreateAPIView):
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

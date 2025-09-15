from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import ChoiceViewSet, QuestionViewSet, VoteAPIView

router = DefaultRouter()
router.register(r"questions", QuestionViewSet, basename="questions")
router.register(r"choices", ChoiceViewSet, basename="choices")

urlpatterns = [
    path("", include(router.urls)),
    path("vote/", VoteAPIView.as_view(), name="vote"),
]

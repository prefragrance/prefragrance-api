from django.urls import path

from review.views import (
    ReviewCreateView,
    ReviewLikeView
)

app_name = "review"

urlpatterns = [
    path("new/", ReviewCreateView.as_view()),
    path("like/", ReviewLikeView.as_view()),
]
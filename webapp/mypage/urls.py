from django.urls import path

from mypage.views import UserProfileAPIView, UserReviewHistoryAPIView, UserFeedbackedHistoryAPIView

app_name = "mypage"

urlpatterns = [
    path("profile/", UserProfileAPIView.as_view()),
    path("review-history/",UserReviewHistoryAPIView.as_view()),
    path("feedback-history/",UserFeedbackedHistoryAPIView.as_view()),
]

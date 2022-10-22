from django.urls import path

from review.views import ReviewDetailView, ReviewLikeView, ReviewView, ReviewHotAPIView

app_name = "review"

urlpatterns = [
    path("", ReviewView.as_view()),
    path("<int:pk>/", ReviewDetailView.as_view()),
    path("<int:review_id>/like/", ReviewLikeView.as_view()),
    path("hot/", ReviewHotAPIView.as_view()),
]

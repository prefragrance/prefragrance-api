from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from review.models import Review


class ReviewLikeView(APIView):
    """ReviewLikeView
    POST: /review/like
    - 해당 리뷰 좋아요 누르기 및 취소
    """

    http_method_names = ["post"]
    permission_classes = [IsAuthenticated]

    def post(self, request, **kwargs):
        user = request.user
        review_id = kwargs.get("review_id")

        review = get_object_or_404(Review, id=review_id)

        if review.liked_users.filter(id=user.id).exists():
            review.liked_users.remove(user)
        else:
            review.liked_users.add(user)

        review.feedback_cnt = review.liked_users.count()
        review.save()

        return Response(status=status.HTTP_200_OK)

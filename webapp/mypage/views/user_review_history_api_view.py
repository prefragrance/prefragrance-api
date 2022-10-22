from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from review.models import Review
from review.serializers import ReviewSerializer
from mypage.serializers import MyPageReviewSerializer

class UserReviewHistoryAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all().prefetch_related(
        "product",
    ).select_related(
        "product__category",
    )
    serializer_class = MyPageReviewSerializer

    def get(self, request, *args, **kwargs):
        review = self.get_queryset().filter(
            user__id = request.user.id
        )
        serializer = self.get_serializer(review,many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

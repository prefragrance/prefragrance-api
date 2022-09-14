from django.db.models import Sum
from rest_framework import status
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Product
from product.permissions import IsOwnerOrReadOnly
from review.models import Review
from review.serializers import ReviewSerializer


class ReviewView(ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        if not Product.objects.filter(id=kwargs.get("id")).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        product = Product.objects.get(id=kwargs.get("id"))
        product.reset_product_review_cnt_and_rate()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ReviewLikeView(APIView):
    http_method_names = ["post"]
    permission_classes = [IsAuthenticated]

    def post(self, request, **kwargs):
        user = request.user
        review_id = kwargs.get("review_id")
        if not Review.objects.filter(id=review_id).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        review = Review.objects.get(id=review_id)

        if review.liked_users.filter(id=user.id).exists():
            review.liked_users.remove(user)
        else:
            review.liked_users.add(user)

        review.feedback_cnt = review.liked_users.count()
        review.save()

        return Response(status=status.HTTP_200_OK)


class ReviewDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

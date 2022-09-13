from django.db.models import Sum
from django.shortcuts import get_object_or_404
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

        product.review_cnt = product.reviews.count()
        rate_sum = product.reviews.aggregate(Sum("rate"))
        product.rate_sum = rate_sum["rate__sum"]
        product.rate = product.rate_sum / product.review_cnt

        product.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ReviewLikeView(APIView):
    http_method_names = ["post"]
    permission_classes = [IsAuthenticated]

    def post(self, request, **kwargs):
        user = request.user
        review_id = kwargs.get("review_id")


        review = get_object_or_404(
            Review,
            id = review_id
        )

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

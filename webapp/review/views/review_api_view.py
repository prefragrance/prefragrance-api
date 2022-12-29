from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from product.models import Product
from product.permissions import IsOwnerOrReadOnly
from review.models import Review
from review.serializers import ReviewPostSerializer, ReviewSerializer


class ReviewView(ListCreateAPIView):
    """ReviewView
    POST: product/<int:id>/review/
    - 상품 리뷰 작성하기
    """

    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewPostSerializer

    def perform_create(self, serializer):
        product = Product.objects.get(id=self.kwargs.get("id"))
        serializer.save(user=self.request.user, product=product)

    def post(self, request, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if not Product.objects.filter(id=kwargs.get("id")).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        product = Product.objects.get(id=kwargs.get("id"))
        product.reset_product_review_cnt_and_rate()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "product_id",
                openapi.IN_QUERY,
                description="Product ID",
                type=openapi.TYPE_NUMBER,
            )
        ]
    )
    def get(self, request, **kwargs):
        if not Product.objects.filter(id=kwargs.get("id")).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        review_ids = self.get_queryset().filter(
        product__id = kwargs.get("id"),
        ).values_list('id', flat=True)

        rate = request.GET.get("rate")
        ordering = request.GET.get("ordering")

        if ordering is not None:
            queryset = self.get_queryset().order_by('-'+ordering)
        else:
            queryset = self.get_queryset()
        queryset = queryset.filter(id__in = review_ids)

        if rate is not None:
            queryset = queryset.filter(rate = rate)
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReviewDetailView(RetrieveUpdateDestroyAPIView):
    """ReviewView
    GET: /review/<int:pk>
    - id에 해당하는 상품 리뷰 불러오기 및 수정, 삭제하기
    """

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

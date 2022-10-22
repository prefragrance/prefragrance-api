from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from product.serializers import ProductSerializer
from product.models import ProductFeedback, Product


class UserFeedbackedHistoryAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all().select_related(
        "category",
    ).prefetch_related(
        "tags",
        "codes",
    )
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        product_ids = ProductFeedback.objects.filter(
            user = request.user
        ).values_list("product__id", flat=True)

        product = self.get_queryset().filter(
            id__in = product_ids
        )
        serializer = self.get_serializer(product, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

from itertools import product
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from datetime import datetime, timedelta
from collections import Counter


from product.models import Product
from product.serializers import ProductSerializer
from accounts.models import Visit
from review.models import Review

class ProductHotAPIView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        """
        url : /product/hot?s=review
        /product/hot?s=visit
        """
        standard = request.GET.get("s")

        end_date = datetime.today()
        start_date = end_date - timedelta(days=7)

        if standard == 'visit':
            product_ids = Visit.objects.filter(
                pub_date__range=[start_date, end_date]
            ).values_list('product__id',flat=True)

        elif standard == 'review':
            product_ids = Review.objects.filter(
                pub_date__range=[start_date, end_date]
            ).values_list('product__id',flat=True)

        counter = Counter(product_ids)
        result_product_ids = []
        for count in counter.most_common(5):
            result_product_ids.append(count[0])

        queryset = self.get_queryset().filter(
            id__in = result_product_ids
        )

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

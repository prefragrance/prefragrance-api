import random
from product.models import Code, Product
from review.models import Review

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from django.db.models import Q
from rest_framework import viewsets

from accounts.models import Visit, User
from product.models import ProductCode
from product.serializers import ProductSerializer





class Recommend(APIView):
    permission_classes = [AllowAny]
    serializer_class = ProductSerializer

    def get(self, request):
        code = request.GET.get('code')
        if code:
            product_ids = ProductCode.objects.filter(
                code__name = code
            ).values_list('product__id', flat=True)
            product = Product.objects.filter(
                id__in = product_ids
            ).order_by('-review_cnt')
            serializer = ProductSerializer(product, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            queryset = Code.objects.all()
            randomCode = random.sample(list(queryset), 6)
            result = []
            for code in randomCode:
                result.append(code.name)
            return Response(result,status=status.HTTP_200_OK)

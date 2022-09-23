import random

from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.permissions import AllowAny

from product.serializers import ProductSerializer
from product.models import Code, Product, ProductCode, ProductTag
from tag.models import Tag


class MagazineAPIView(ListAPIView):
    '''
    매거진 api
    /product?code=코드명
    /product?tag=태그명
    /product => 랜덤으로 코드/태그 추출
    '''
    permission_classes = [AllowAny]
    serializer_class = ProductSerializer
    queryset = (
        Product.objects.all()
        .select_related(
            "category",
        )
        .prefetch_related("tags", "codes")
    )

    def get(self, request):
        code = request.GET.get('code')
        tag = request.GET.get('tag')
        if not code and not tag:
            codes = Code.objects.all()
            randomCode = random.sample(list(codes), 2)
            tags = Tag.objects.all()
            randomTag = random.sample(list(tags),2)
            result = {
                'codes':[],
                'tags':[],
            }

            for i in range(2):
                result['codes'].append(randomCode[i].name)
                result['tags'].append(randomTag[i].name)
            return Response(result,status=status.HTTP_200_OK)

        elif code:
            product_ids = ProductCode.objects.filter(
                code__name = code
            ).values_list('product__id', flat=True)

        elif tag:
            product_ids = ProductTag.objects.filter(
                tag__name = tag
            ).values_list('product__id', flat=True)

        product = self.get_queryset().filter(
            id__in = product_ids
        ).order_by('-review_cnt')

        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

import random
from collections import Counter

from django.contrib.contenttypes.models import ContentType
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from taggit.models import Tag, TaggedItem

from product.models import Code, Product, ProductCode
from product.serializers import ProductSerializer
from review.models import Review


class MagazineAPIView(ListAPIView):
    """
    매거진 api
    /product/magazine/?code=코드명
    /product/magazine/?tag=태그명
    /product/magazine/?season=계절명
    /product/magazine => 랜덤으로 코드/태그 추출
    """

    permission_classes = [AllowAny]
    serializer_class = ProductSerializer
    queryset = (
        Product.objects.all().select_related("category").prefetch_related("codes")
    )

    def get(self, request):
        code = request.GET.get("code")
        tag = request.GET.get("tag")
        season = request.GET.get("season")
        products = self.filter_queryset(self.get_queryset())
        c_type = ContentType.objects.get(app_label="product", model="product")

        if not code and not tag and not season:
            codes = Code.objects.all()
            randomCode = random.sample(list(codes), 2)
            tags = Tag.objects.all()
            randomTag = random.sample(list(tags), 2)
            result = {
                "codes": [],
                "tags": [],
            }

            for i in range(2):
                result["codes"].append(randomCode[i].name)
                result["tags"].append(randomTag[i].name)
            return Response(result, status=status.HTTP_200_OK)

        elif code:
            product_ids = ProductCode.objects.filter(code__name=code).values_list(
                "product__id", flat=True
            )

        elif tag:
            product_ids = TaggedItem.objects.filter(
                tag__name=tag, content_type=c_type
            ).values_list("object_id", flat=True)

        elif season:
            product_id = Review.objects.filter(season=season).values_list(
                "product__id", flat=True
            )
            counter = Counter(product_id)
            product_ids = []
            for count in counter.most_common(5):
                product_ids.append(count[0])

        product = products.filter(id__in=product_ids).order_by("-review_cnt")

        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

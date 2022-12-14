import random
from collections import Counter

from django.db.models import Q
from product.models.product_feedback import ProductFeedback
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from accounts.models import User
from product.models import Product
from product.serializers import ProductSerializer


class MagazineUserAPIView(ListAPIView):
    """
    매거진 유저 based api
    GET: /product/user-magazine
    => 로그인 된 유저의 경우, 성별과 나이대에 맞는
    다른 유저의 좋아요 상품 목록 불러오기
    로그인 되지 않은 유의 경우, 랜덤으로 불러오기
    """

    permission_classes = [AllowAny]
    serializer_class = ProductSerializer
    queryset = (
        Product.objects.all()
        .select_related(
            "category",
        )
        .prefetch_related("codes")
    )

    def get(self, request):
        products = self.filter_queryset(self.get_queryset())
        user = request.user
        if user.is_authenticated:
            gender = user.gender
            start_age = (user.age // 10) * 10
        else:
            gender = random.choice(["M", "F", "NB"])
            start_age = random.randint(1, 6) * 10
        last_age = start_age + 9
        result = {"age": [start_age], "gender": [gender]}
        if start_age < 60:
            user_ids = User.objects.filter(
                Q(gender=gender) & Q(age__range=[start_age, last_age])
            )
        else:
            user_ids = User.objects.filter(Q(gender=gender) & Q(age__gte=60))

        product_ids = ProductFeedback.objects.filter(user_id__in=user_ids).values_list(
            "product__id", flat=True
        )
        counter = Counter(product_ids)
        product_id = []
        for count in counter.most_common(5):
            product_id.append(count[0])
        queryset = products.filter(id__in=product_id)
        serializer = self.get_serializer(queryset, many=True)

        return Response([result, serializer.data], status=status.HTTP_200_OK)

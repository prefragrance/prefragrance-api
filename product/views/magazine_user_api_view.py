from collections import Counter

from django.db.models import Q
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from accounts.models import User
from product.models import Product
from product.models.product_feedback import ProductFeedback
from product.serializers import ProductSerializer


class MagazineUserAPIView(ListAPIView):
    """
    매거진 유저 based api
    GET: /product/user
    => 로그인 된 유저의 성별과 나이대에 맞는
    다른 유저의 좋아요 상품 목록 불러오기
    """

    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = (
        Product.objects.all()
        .select_related(
            "category",
        )
        .prefetch_related("tags", "codes")
    )

    def get(self, request):
        products = self.filter_queryset(self.get_queryset())
        user = request.user
        gender = user.gender
        start_age = (user.age // 10) * 10
        last_age = start_age + 9
        user_ids = User.objects.filter(
            Q(gender=gender) & Q(age__range=[start_age, last_age])
        )
        product_ids = ProductFeedback.objects.filter(user_id__in=user_ids).values_list(
            "product__id", flat=True
        )
        counter = Counter(product_ids)
        product_id = []
        for count in counter.most_common(5):
            product_id.append(count[0])
        queryset = products.filter(id__in=product_id)
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

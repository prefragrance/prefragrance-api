from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Product


class ProductLikeView(APIView):
    """ProductLikeView
    POST: /product/<int:id>/like
    - 해당 상품 좋아요 누르기 및 취소
    """

    http_method_names = ["post"]
    permission_classes = [IsAuthenticated]

    def post(self, request, **kwargs):
        user = request.user
        product_id = kwargs.get("id")
        if not Product.objects.filter(id=product_id).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        product = Product.objects.get(id=product_id)

        if product.liked_users.filter(id=user.id).exists():
            product.liked_users.remove(user)
        else:
            product.liked_users.add(user)

        product.feedback_cnt = product.liked_users.count()
        product.save()

        return Response(status=status.HTTP_200_OK)

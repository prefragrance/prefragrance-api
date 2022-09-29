from datetime import datetime

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import (authentication_classes,
                                       permission_classes)
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import User, Visit
from product.models import Product
from product.serializers import ProductDetailSerializer


class ProductDetailView(RetrieveAPIView):
    """ProductDetailView
    GET: /product/<int:id>
    - product id에 해당하는 상품을 가져오기
    """

    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer

    def get(self, request, **kwargs):
        product_id = kwargs.get("id")
        product = get_object_or_404(self.get_queryset(), id=product_id)
        serializer = self.get_serializer(product)
        user = request.user

        # 로그인이 되어 있는 경우
        if request.user.is_authenticated:
            cookie_name = f"hit:{user.id}"
            visit, is_visit = Visit.objects.get_or_create(
                user=User.objects.get(id=user.id),
                product=Product.objects.get(id=product_id),
            )
            if not is_visit:
                visit.pub_date = datetime.now()
                visit.save()
        # 로그인이 안 되어 있는 경우
        else:
            cookie_name = "hit"

        tomorrow = datetime.replace(datetime.now(), hour=23, minute=59, second=0)
        expires = datetime.strftime(tomorrow, "%a, %d-%b-%Y %H:%M:%S GMT")

        response = Response(serializer.data, status=status.HTTP_200_OK)

        # 쿠키 읽기 & 생성
        if request.COOKIES.get(cookie_name) is not None:  # 쿠키에 hit 값이 이미 있을 경우
            cookies = request.COOKIES.get(cookie_name)
            cookies_list = cookies.split("|")
            if str(product_id) not in cookies_list:
                product.visit_cnt += 1
                product.save()
                response.set_cookie(
                    cookie_name, cookies + f"|{product_id}", expires=expires
                )  # 쿠키 생성

        else:  # 쿠키에 hit 값이 없을 경우(즉 현재 보는 게시글이 첫 게시글임)
            product.visit_cnt += 1
            product.save()
            response.set_cookie(cookie_name, product_id, expires=expires)

        return response

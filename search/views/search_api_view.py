from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from datetime import datetime
from django.db.models import Q

from search.serializers import (
    ProductSearchSerializer,
)
from search.models import (
    Search,
)

from product.models import Product, ProductTag, Category
from tag.models import Tag

class SearchAPIView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSearchSerializer
    filter_backends = [
        OrderingFilter,
        SearchFilter,
        DjangoFilterBackend,
    ]

    def get(self, request):
        """SearchAPIView
        GET: /search?tab=recommend
        - tab 에 따라서 검색어가 반환된다
        """

        #검색어가 없을 경우에는 전체
        products = self.get_queryset()

        q_field = request.GET.get("q_field")
        q = request.GET.get("q")
        category = request.GET.get("c")
        standard = request.GET.get("s")

        # 제품명으로 검색하는 경우
        if q_field == 'name':
            products = Product.objects.filter(
                Q(name__contains=q))

        # 제조사로 검색하는 경우
        elif q_field == 'producer':
            products = Product.objects.filter(
                Q(producer__contains=q))

        # 태그로 검색하는 경우
        elif q_field == 'tag':
            tag = Tag.objects.filter(Q(name__contains=q))
            product_tags = ProductTag.objects.filter(
                tag__in = tag,
            ).values_list('product', flat=True)

            #해당하는 태그가 있다면
            if product_tags:
                products = Product.objects.filter(
                    id__in = product_tags
                ).values_list('id',flat=True)

            else:
            #태그가 없으면 전체
                products = self.get_queryset()

        #카테고리별로 분류
        if category:
            category = Category.objects.filter(name=category)
            products = products.filter(
                category__in = category
            )

        #기준에 맞게 정렬하기
        if standard == 'star':
            products = Product.objects.filter(
            id__in = products
        ).order_by('-rate')
        elif standard == 'view':
            products = Product.objects.filter(
            id__in = products
        ).order_by('-view')
        elif standard == 'review':
            products = Product.objects.filter(
            id__in = products
        ).order_by('-review')

        #페이지네이션
        page = self.paginate_queryset(products)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        q = request.GET.get("q")

        #로그인 되어 있는 경우
        if request.user.is_authenticated:

            #검색어가 일치하는 객체 있는지 확인
            search = Search.objects.filter(
                content = q
            )

            search_id = Search.objects.filter(
                content = q
            ).values_list('id')

            #있으면 하나 증가
            if search:
                print(search)
                search[0].cnt += 1
                search[0].save()
            #     user_search = UserSearch.objects.filter(
            #     user = request.user,
            #     search_id__in = search_id
            # )

                # #이미 그 검색어를 검색한 적이 있으면 
                # if user_search:
                #     user_search[0].pub_date = datetime.now()
                #     user_search[0].save()
                # else:
                #     user_search = UserSearch(
                #         user = request.user,
                #         search = search,
                #         pub_date = datetime.now()
                #     )

            #없으면 새로 생성
            else:
                search = Search.objects.create(content = q, cnt = 0)
                # UserSearch.objects.create(
                #         user = request.user,
                #         search = search,
                #         pub_date = datetime.now()
                #         )

            return Response(status=status.HTTP_201_CREATED)

        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

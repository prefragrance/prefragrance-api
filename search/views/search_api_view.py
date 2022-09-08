from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from datetime import datetime
from django.db.models import Q
from search.models import RecommendSearch

from search.serializers import SearchSerializer, RecommendSearchSerializer
from product.serializers import ProductSerializer
from search.models import Search

from product.models import Product, ProductTag, Category
from tag.models import Tag

class SearchAPIView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [
        OrderingFilter,
        SearchFilter,
        DjangoFilterBackend,
    ]
    search_fields = [
                     'name',
                     'producer',
                     'tags__name',
                     'codes__name',
                     'category__name'
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
        tab = request.GET.get("tab")
        category = request.GET.get("c")

        if tab:
            if tab == "popular":
                queryset = Search.objects.all()[:4]
                serializer = SearchSerializer(queryset, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif tab == "recommend":
                queryset = RecommendSearch.objects.all()
                serializer = RecommendSearchSerializer(queryset, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)

        if category:
            category = Category.objects.filter(name=category)
            products = products.filter(
                category__in = category
            )

        if q_field == 'name':
            product_ids = Product.objects.filter(
                Q(name__contains=q))

        elif q_field == 'producer':
            product_ids = Product.objects.filter(
                Q(producer__contains=q))

        elif q_field == 'tag':
            tag = Tag.objects.filter(Q(name__contains=q))
            product_ids = ProductTag.objects.filter(
                tag__in = tag,
            ).values_list('product__id', flat=True)
        else:
            products = self.filter_queryset(self.get_queryset())

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
            search, is_created = Search.objects.get_or_create(
                content = q
            )

            search.increment_search_count()

            return Response(status=status.HTTP_201_CREATED)

        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

from collections import Counter
from datetime import datetime, timedelta

from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from product.models import Category, Product, ProductTag
from product.serializers import ProductSerializer
from search.models import RecommendSearch, SearchLog
from search.serializers import RecommendSearchSerializer
from tag.models import Tag


class SearchAPIView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = (
        Product.objects.all()
        .select_related(
            "category",
        )
        .prefetch_related("tags", "codes")
    )

    serializer_class = ProductSerializer
    filter_backends = [
        OrderingFilter,
        SearchFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["name", "producer", "tags__name", "category__name"]

    def get(self, request):
        """SearchAPIView
        GET: /search?tab=recommend
        - tab 에 따라서 검색어가 반환된다
        """

        products = self.filter_queryset(self.get_queryset())

        q_field = request.GET.get("q_field")
        search = request.GET.get("search")
        tab = request.GET.get("tab")
        category = request.GET.get("c")

        if tab == "popular":
            end_date = datetime.today()
            start_date = end_date - timedelta(days=7)

            search_words = SearchLog.objects.filter(
                pub_date__range=[start_date, end_date]
            ).values_list("content", flat=True)

            counter = Counter(search_words)
            result_words = []
            for word in counter.most_common(4):
                result_words.append(word[0])

            return Response(result_words, status=status.HTTP_200_OK)

        elif tab == "recommend":
            queryset = RecommendSearch.objects.all()
            serializer = RecommendSearchSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        if category:
            products = products.filter(category__name=category)

        if q_field == "name":
            product_ids = Product.objects.filter(Q(name__contains=search))

            products = products.filter(id__in=product_ids)
        elif q_field == "producer":
            product_ids = Product.objects.filter(Q(producer__contains=search))
            products = products.filter(id__in=product_ids)

        elif q_field == "tag":
            tag = Tag.objects.filter(Q(name__contains=search))
            product_ids = ProductTag.objects.filter(
                tag__in=tag,
            ).values_list("product__id", flat=True)
            products = products.filter(id__in=product_ids)

        page = self.paginate_queryset(products)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        search_word = request.GET.get("search")

        if search_word is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        cookie_name = "search"

        cookie_value = search_word.encode("utf-8")

        one_hour = datetime.replace(datetime.now(), hour=23, minute=59, second=0)
        expires = datetime.strftime(one_hour, "%a, %d-%b-%Y %H:%M:%S GMT")

        response = Response(status=status.HTTP_201_CREATED)

        if request.COOKIES.get(cookie_name) is not None:
            cookies = request.COOKIES.get(cookie_name)
            cookies_list = cookies.split("|")

            if str(cookie_value) not in cookies_list:
                SearchLog(content=search_word, pub_date=datetime.now()).save()
                response.set_cookie(
                    cookie_name, cookies + f"|{cookie_value}", expires=expires
                )

        else:
            SearchLog(content=search_word, pub_date=datetime.now()).save()

            response.set_cookie(cookie_name, cookie_value, expires=expires)

        return response

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

from datetime import date, datetime
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

from search.serializers import (
    RecommendSearchSerializer,
    SearchSerializer,
    UserSearchSerializer,
    ProductSearchSerializer,
    TagSearchSerializer,
)
from search.models import (
    Search,
    RecommendSearch,
    UserSearch,
)

from product.models import Product, ProductTag, Category

from account.models import User


from tag.models import Tag

class SearchAPIView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSearchSerializer

    def get(self, request):
        """SearchAPIView
        GET: /search?tab=recommend
        - tab 에 따라서 검색어가 반환된다
        """

        queryset = self.get_queryset()

        q_field = request.GET.get("q_field")
        q = request.GET.get("q")
        category = request.GET.get("c")
        standard = request.GET.get("s")

        if q_field and q and category:

            # 제품명으로 검색하는 경우
            if q_field == 'name':
                products = Product.objects.filter(
                    Q(name__contains=q))

            # 제조사로 검색하는 경우
            elif q_field == 'producer':
                products = Product.objects.filter(Q(producer__contains=q))

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

        else:
            products = self.get_queryset()

        #검색어가 없을 경우에는 전체
        category = Category.objects.filter(name=category)
        products = products.filter(
            category__in = category
        )

        products = Product.objects.filter(
            id__in = products
        )

        if standard == 'star':
            products.order_by('rate')
        elif standard == 'view':
            products.order_by('visit_cnt')
        elif standard == 'review':
            products.order_by('review_cnt')

        # product_tags = ProductTag.objects.filter(
        #     product__in = products,
        # ).values_list('tag', flat=True)

        # tags = Tag.objects.filter(
        #     id__in = product_tags
        # )

        serializer = self.get_serializer(products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # @csrf_exempt
    # def post(self, request):
    #     q_field = request.GET.get("q_field")
    #     q = request.GET.get("q")
    #     category = request.GET.get("c")

    #     #로그인 되어 있는 경우
    #     if request.user.is_authenticated:
    #         print("로그인")

    #         #검색어가 일치하는 객체 있는지 확인
    #         search = Search.objects.filter(content = q)

    #         #있으면 하나 증가
    #         if search:
    #             search[0].cnt += 1
    #             print(111111)
    #             user_search = UserSearch.objects.filter(
    #             # user = None,
    #             search = search
    #         )
    #             print(22222)

    #             if user_search:
    #                 user_search[0].pub_date = datetime.now()
    #             else:
    #                 user_search = UserSearch(
    #                     user = None,
    #                     search = search,
    #                     pub_date = datetime.now()
    #                 )

    #         #없으면 새로 생성
    #         else:
    #             search = Search(content = q,
    #                             cnt = 0)
    #             user_search = UserSearch(
    #                     user = None,
    #                     search = search,
    #                     pub_date = datetime.now()
    #                     )
    #         return Response(status=status.HTTP_201_OK)

    #     else:
    #         print("여기")
    #         return Response(status=status.HTTP_403_FORBIDDEN)

        # tab = request.GET.get("tab")
        # if tab:
        #     if tab == 'recommend':
        #         queryset = RecommendSearch.objects.all()
        #         serializer = RecommendSearchSerializer(queryset, many=True)

        #     elif tab == 'popular':
        #         queryset = Search.objects.all()
        #         queryset.order_by('cnt')[:4]
        #         serializer = SearchSerializer(queryset, many=True)

        #     elif tab == 'recent':
        #         if request.user.is_authenticated:
        #             queryset = UserSearch.objects.filter(
        #                 user = request.user,
        #             )
        #             if queryset is None:
        #                 return Response(status=status.HTTP_200_OK)
        #             queryset.order_by('-pub_date')[:4]
        #             serializer = UserSearchSerializer(queryset, many=True)
        #         # 로그인 안된 경우에는 프론트에서 처리

        #     elif tab != None:
        #         #없는 탭을 요청하는 경우
        #         return Response(status=status.HTTP_400_BAD_REQUEST)


        # tab
        # return Response(serializer.data, status=status.HTTP_200_OK)

        #  = request.GET.get("tab")

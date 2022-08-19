# from rest_framework.generics import ListAPIView
# from rest_framework.response import Response
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework import status

# from datetime import date, datetime
# from django.shortcuts import get_object_or_404

# from search.serializers import (
#     RecommendSearchSerializer,
#     SearchSerializer,
#     UserSearchSerializer,
#     ProductSearchSerializer,
#     TagSearchSerializer,
# )
# from search.models import (
#     Search,
#     RecommendSearch,
#     UserSearch,
#     UserProductSearch,
# )

# from product.models import Product, ProductTag, Category

# from account.models import User, user


# from tag.models import Tag

# class SearchRetrieveAPIView(ListAPIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request, product_id):

#         # 유저가 최근 찾은 향을 저장하기 위한 메서드
#         product = get_object_or_404(Product, id=product_id)
#         try:
#             user_product_search = UserProductSearch.objects.filter(
#                 user = request.user,
#                 product = product,
#             )

#             if user_product_search:
#                 user_product_search.pub_date = datetime.now()

#         except:
#             UserProductSearch(
#                 user = request.user,
#                 product = product,
#                 pub_date = datetime.now()
#             )

#         return Response(status=status.HTTP_201_CREATED)

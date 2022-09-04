#현재 migrate부터 해야 함!

from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from datetime import datetime, timezone

from product.permissions import IsOwnerOrReadOnly

from product.serializers import ProductDetailSerializer
from product.models import Product

class ProductDetailView(RetrieveAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    
    def get(self, request, **kwargs):
        product_id = kwargs.get('id')
        queryset = Product.objects.get(id=product_id)
        serializer = ProductDetailSerializer(queryset)

        tomorrow = datetime.replace(datetime.now(), hour=23, minute=59, second=0)
        expires = datetime.strftime(tomorrow, "%a, %d-%b-%Y %H:%M:%S GMT")
        
        response = Response(serializer.data, status=status.HTTP_200_OK)
        
        # # 쿠키 읽기 & 생성
        # if request.COOKIES.get('hit') is not None: # 쿠키에 hit 값이 이미 있을 경우
        #     cookies = request.COOKIES.get('hit')
        #     cookies_list = cookies.split('|') # '|'는 다르게 설정 가능 ex) '.'
        #     if str(product_id) not in cookies_list:
        #         queryset.visit_cnt += 1
        #         queryset.save()
        #         response.set_cookie('hit', cookies+f'|{product_id}', expires=expires) # 쿠키 생성
                    
        # else: # 쿠키에 hit 값이 없을 경우(즉 현재 보는 게시글이 첫 게시글임)
        #     queryset.visit_cnt += 1
        #     queryset.save()
        #     response.set_cookie('hit', product_id, expires=expires)

        return response


                
class ProductLikeView(APIView):
    http_method_names = ['post']
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, **kwargs):
        user = request.user
        product_id = kwargs.get('id')
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
        
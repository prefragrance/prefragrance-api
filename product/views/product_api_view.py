from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from datetime import datetime, timezone

from product.permissions import IsOwnerOrReadOnly

from accounts.models import Visit, User
from product.serializers import ProductDetailSerializer
from product.models import Product

class ProductDetailView(RetrieveAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    
    def get(self, request, **kwargs):
        product_id = kwargs.get('id')
        product = get_object_or_404(self.get_queryset(), id=product_id)
        serializer = self.get_serializer(product)
        user = request.user

        # 로그인이 되어 있는 경우
        if request.user.is_authenticated:
            cookie_name = f'hit:{user.id}'
            visit, is_visit = Visit.objects.get_or_create(
                user = User.objects.get(id=user.id),
                product = Product.objects.get(id=product_id)
            )
            if not is_visit:
                visit.pub_date = datetime.now()
                visit.save()
        # 로그인이 안 되어 있는 경우
        else:
            cookie_name = 'hit'

        tomorrow = datetime.replace(datetime.now(), hour=23, minute=59, second=0)
        expires = datetime.strftime(tomorrow, "%a, %d-%b-%Y %H:%M:%S GMT")
        
        response = Response(serializer.data, status=status.HTTP_200_OK)
        
        # 쿠키 읽기 & 생성
        if request.COOKIES.get(cookie_name) is not None: # 쿠키에 hit 값이 이미 있을 경우
            cookies = request.COOKIES.get(cookie_name)
            cookies_list = cookies.split('|') 
            if str(product_id) not in cookies_list:
                product.visit_cnt += 1
                product.save()
                response.set_cookie(cookie_name, cookies+f'|{product_id}', expires=expires) # 쿠키 생성
                    
        else: # 쿠키에 hit 값이 없을 경우(즉 현재 보는 게시글이 첫 게시글임)
            product.visit_cnt += 1
            product.save()
            response.set_cookie(cookie_name, product_id, expires=expires)

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
        
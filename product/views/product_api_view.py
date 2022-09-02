from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from product.permissions import IsOwnerOrReadOnly

from product.serializers import ProductSerializer
from product.models import Product

# ip를 리턴해주는 함수
# def get_client_ip(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return ip

class ProductDetailView(RetrieveAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    
    def get(self, request, **kwargs):
        product_id = kwargs.get('id')
        queryset = Product.objects.get(id=product_id)
        serializer = ProductSerializer(queryset)

        # ip를 이용해서 조회수 기능 만들고 저장 (visit모델에서 user_ip 필요(?)
        # ip = get_client_ip(request)

        # if not Visit.objects.filter(user_ip=ip, product=id).exists():
        #     product.visit_cnt += 1 
        #     product.save()

        #     Visit.objects.create(
        #         user = self.request.user,
        #         user_ip = ip,
        #         product = product
        # )

        return Response(serializer.data)


                
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
        
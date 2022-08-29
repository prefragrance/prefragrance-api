from django.shortcuts import get_object_or_404
from django.db.models import Sum
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from product.permissions import IsOwnerOrReadOnly

from product.serializers import ProductSerializer
from product.models import Product, ProductFeedback
from review.models import Review

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
    def get_object(self, id):
        product = get_object_or_404(Product, id = id)
        return product
    
    def get(self, request, id):
        product = self.get_object(id)
        product.visit_cnt += 1
        product.review_cnt = product.reviews.count()
        rate_sum = Review.objects.filter(product=id).aggregate(Sum('rate'))
        product.rate_sum = rate_sum['rate__sum']
        product.feedback_cnt = product.feedbacks.count()
        product.rate = product.rate_sum / product.review_cnt
        product.save()
        serializer = ProductSerializer(product)

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

    def post(self, request, *arg, **kwargs):
        like, created = ProductFeedback.objects.get_or_create(
            user = self.request.user,
            product = self.kwargs.get('id')
        )
        if not created:
            like.delete()
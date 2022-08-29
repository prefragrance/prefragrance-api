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
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from review.serializers import ReviewSerializer
from review.models import Review, ReviewFeedback


class ReviewCreateView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class ReviewLikeView(APIView):
    http_method_names = ['post']
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *arg, **kwargs):
        like, created = ReviewFeedback.objects.get_or_create(
            user = self.request.user,
            product = self.kwargs.get('id')
        )
        if not created:
            like.delete()
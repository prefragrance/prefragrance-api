from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta

from review.models import Review
from review.serializers import ReviewSerializer

class ReviewHotAPIView(ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        end_date = datetime.today()
        start_date = end_date - timedelta(days=7)

        review_ids = Review.objects.filter(
            pub_date__range=[start_date,end_date]
        ).values_list('id', flat=True)

        queryset = self.get_queryset().filter(
            id__in = review_ids
        ).order_by('-feedback_cnt')[:6]

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

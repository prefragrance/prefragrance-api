from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta
from collections import Counter

from review.models import Review, ReviewFeedback
from review.serializers import ReviewSerializer

class ReviewHotAPIView(ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        end_date = datetime.today()
        start_date = end_date - timedelta(days=7)

        review_ids = ReviewFeedback.objects.filter(
            pub_date__range=[start_date,end_date]
        ).values_list('review__id', flat=True)

        counter = Counter(review_ids)
        result_review_ids = []
        for count in counter.most_common(6):
            result_review_ids.append(count[0])

        queryset = self.get_queryset().filter(
            id__in = result_review_ids
        ).order_by('-feedback_cnt')[:6]

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

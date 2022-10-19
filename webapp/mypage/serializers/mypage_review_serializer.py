from rest_framework import serializers

from review.models import Review
from product.serializers import ProductSerializer

class MyPageReviewSerializer(serializers.ModelSerializer):

    product = ProductSerializer(
        read_only=False,
    )

    class Meta:
        model = Review
        fields = [
            "id",
            "user",
            "product",
            "season",
            "time",
            "duration",
            "strength",
            "content",
            "rate",
            "pub_date",
            "feedback_cnt",
        ]
        read_only_fields = [
            "id",
            "user",
            "pub_date",
            "feedback_cnt",
            "product",
        ]

from rest_framework import serializers

from review.models import Review


class ReviewSerializer(serializers.ModelSerializer):
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
            "product",
            "pub_date",
            "feedback_cnt",
        ]

from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField

from review.models import Review


class ReviewPostSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

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
            "tags",
        ]
        read_only_fields = [
            "id",
            "user",
            "product",
            "pub_date",
            "feedback_cnt",
        ]

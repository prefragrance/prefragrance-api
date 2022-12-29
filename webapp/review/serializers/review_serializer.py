from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField

from review.models import Review


class ReviewSerializer(TaggitSerializer, serializers.ModelSerializer):
    nickname = serializers.CharField(source='user.nickname')
    profile_img = serializers.ImageField(source='user.profile_img')

    class Meta:
        model = Review
        fields = [
            "id",
            "nickname",
            "profile_img",
            "content",
            "pub_date",
            "feedback_cnt",
            "rate",
        ]
        read_only_fields = [
            "id",
            "nickname",
            "profile_img",
            "content",
            "pub_date",
            "feedback_cnt",
            "rate",
        ]

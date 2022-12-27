from product.serializers.code_serializer import CodeSerializer
from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField

from product.models import Product


class ProductDetailSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    category = serializers.CharField(source="category.name")

    codes = CodeSerializer(
        read_only=False,
        many=True,
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "category",
            "name",
            "producer",
            "tags",
            "codes",
            "feedback_cnt",
            "review_cnt",
            "visit_cnt",
            "thumbnail_url",
            "rate_sum",
            "rate",
            "liked_users",
        ]

        read_only_fields = [
            "id",
            "feedback_cnt",
            "review_cnt",
            "visit_cnt",
            "rate_sum",
            "rate",
        ]

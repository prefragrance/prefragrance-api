from product.serializers.code_serializer import CodeSerializer
from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField

from product.models import Category, Product


class ProductSerializer(TaggitSerializer, serializers.ModelSerializer):
    """Serializer definition for Product Model."""

    tags = TagListSerializerField()

    category = serializers.CharField(source="category.name")

    codes = CodeSerializer(
        read_only=False,
        many=True,
    )

    class Meta:
        """Meta definition for ProductSerializer."""

        model = Product
        fields = [
            "id",
            "name",
            "producer",
            "category",
            "feedback_cnt",
            "review_cnt",
            "visit_cnt",
            "thumbnail_url",
            "rate_sum",
            "rate",
            "tags",
            "codes",
        ]

        read_only_fields = [
            "id",
            "name",
            "producer",
            "category",
            "feedback_cnt",
            "review_cnt",
            "visit_cnt",
            "thumbnail_url",
            "rate_sum",
            "rate",
            "tags",
            "codes",
        ]

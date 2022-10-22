from rest_framework import serializers

from product.models import Category, Product
from tag.serializers import TagSerializer
from product.serializers.code_serializer import CodeSerializer

class ProductSerializer(serializers.ModelSerializer):
    """Serializer definition for Product Model."""

    tags = TagSerializer(
        read_only=False,
        many=True,
    )

    category = serializers.CharField(
        source = "category.name"
    )

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

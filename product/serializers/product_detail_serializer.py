from rest_framework import serializers

from product.models import Product
from product.serializers.code_serializer import CodeSerializer
from tag.serializers import TagSerializer
from review.serializers import ReviewSerializer

class ProductDetailSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    tags = TagSerializer(
        read_only=False,
        many=True,
    )

    category = serializers.CharField(
        source = 'category.name'
    )

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
            "thumbnail_url",
            "rate_sum",
            "rate",
            "liked_users",
            "reviews",
        ]

        read_only_fields = [
            "id",
            "feedback_cnt",
            "review_cnt",
            "visit_cnt",
            "rate_sum",
            "rate",
        ]

from rest_framework.serializers import ModelSerializer

from product.models import Category, Product
from tag.serializers import TagSerializer


class CategorySerializer(ModelSerializer):
    """Serializer definition for Category Model"""

    model = Category
    fields = ["name"]
    read_only_fields = ["name"]


class ProductSerializer(ModelSerializer):
    """Serializer definition for Product Model."""

    tags = TagSerializer(
        read_only=False,
        many=True,
    )

    category = CategorySerializer(
        read_only=True,
        many=False,
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
        ]

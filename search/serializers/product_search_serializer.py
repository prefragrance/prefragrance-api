from rest_framework.serializers import ModelSerializer

from product.models import Product

from tag.models import Tag
from tag.serializers import TagSerializer

class ProductSearchSerializer(ModelSerializer):
    """Serializer definition for ProductSearch Model."""

    tags = TagSerializer(
        read_only = False,
        many = True,
    )

    class Meta:
        """Meta definition for ProductSearchSerializer."""

        model = Product
        fields = ["id", "name", "producer", "feedback_cnt", "review_cnt",
                  "visit_cnt", "thumbnail_url", "rate_sum", "rate", "tags"]

        read_only_fields = ["id", "name", "producer", "feedback_cnt", "review_cnt",
                  "visit_cnt", "thumbnail_url", "rate_sum", "rate",  "tags"]

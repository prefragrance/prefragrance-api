from rest_framework.serializers import ModelSerializer

from product.models import Product

from tag.serializers import TagSerializer

class ProductSerializer(ModelSerializer):
    """Serializer definition for Product Model."""

    tags = TagSerializer(
        read_only = False,
        many = True,
    )

    class Meta:
        """Meta definition for ProductSerializer."""

        model = Product
        fields = ["id", "name", "producer", "feedback_cnt", "review_cnt",
                  "visit_cnt", "thumbnail_url", "rate_sum", "rate", "tags"]

        read_only_fields = ["id", "name", "producer", "feedback_cnt", "review_cnt",
                  "visit_cnt", "thumbnail_url", "rate_sum", "rate",  "tags"]

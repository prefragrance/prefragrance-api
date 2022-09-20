from rest_framework.serializers import ModelSerializer

from product.models import Product

from product.models import Code

from tag.serializers import TagSerializer

class MagazineSerializer(ModelSerializer):
    """Serializer definition for Magazine Model."""

    tags = TagSerializer(
        read_only = False,
        many = True,
    )

    class Meta:
        """Meta definition for ProductSerializer."""

        model = Code
        fields = ["id", "name", "producer", "feedback_cnt", "review_cnt",
                  "visit_cnt", "thumbnail_url", "rate_sum", "rate", "tags"]

        read_only_fields = ["id", "name", "producer", "feedback_cnt", "review_cnt",
                  "visit_cnt", "thumbnail_url", "rate_sum", "rate",  "tags"]

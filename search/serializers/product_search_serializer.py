from rest_framework.serializers import ModelSerializer

from product.models import Product

from tag.models import Tag

#인기 검색어에 사용 => cnt 기준으로 나열

class TagSearchSerializer(ModelSerializer):
    """Serializer definition for Tag Model."""

    class Meta:
        """Meta definition for TagSerializer."""

        model = Tag
        fields = ["id", "name"]
        read_only_fields = ["id", "name"]

class ProductSearchSerializer(ModelSerializer):
    """Serializer definition for ProductSearch Model."""

    # tags = TagSearchSerializer(
    #     read_only = False,
    #     required = True,
    # )

    class Meta:
        """Meta definition for ProductSearchSerializer."""

        model = Product
        fields = ["id", "name", "producer", "feedback_cnt", "review_cnt",
                  "visit_cnt", "thumbnail_url", "rate_sum", "rate"]

        read_only_fields = ["id", "name", "producer", "feedback_cnt", "review_cnt",
                  "visit_cnt", "thumbnail_url", "rate_sum", "rate"]

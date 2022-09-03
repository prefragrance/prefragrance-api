from rest_framework.serializers import ModelSerializer

from search.models import Search


class SearchSerializer(ModelSerializer):
    """Serializer definition for Search Model."""

    class Meta:
        """Meta definition for RecommendSearchSerializer."""

        model = Search
        fields = ["id", "content"]
        read_only_fields = ["id", "content"]


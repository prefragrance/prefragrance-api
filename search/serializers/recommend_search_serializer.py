from rest_framework.serializers import ModelSerializer

from search.models import RecommendSearch


class RecommendSearchSerializer(ModelSerializer):
    """Serializer definition for RecommendSearch Model."""

    class Meta:
        """Meta definition for RecommendSearchSerializer."""

        model = RecommendSearch
        fields = ["content"]
        read_only_fields = ["content"]

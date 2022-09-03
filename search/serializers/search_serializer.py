from rest_framework.serializers import ModelSerializer

from search.models import Search, RecommendSearch

class SearchSerializer(ModelSerializer):
    """Serializer definition for Search Model."""

    class Meta:
        """Meta definition for RecommendSearchSerializer."""

        model = Search
        fields = ["id", "content"]
        read_only_fields = ["id", "content"]

# class UserSearchSerializer(ModelSerializer):
#     """Serializer definition for UserSearch Model."""

#     search = SearchSerializer(
#         # read_only = True,
#         required = True,
#     )

#     class Meta:
#         """Meta definition for RecommendSearchSerializer."""

#         model = UserSearch
#         fields = ["id", "user", "search"]
#         read_only_fields = ["id", "cnt", "content"]

class RecommendSearchSerializer(ModelSerializer):
    """Serializer definition for RecommendSearch Model."""

    class Meta:
        """Meta definition for RecommendSearchSerializer."""

        model = RecommendSearch
        fields = ["id", "content"]
        read_only_fields = ["id", "content"]

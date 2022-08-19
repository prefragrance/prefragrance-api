from rest_framework.serializers import ModelSerializer

from search.models import Search, UserSearch, RecommendSearch

#인기 검색어에 사용 => cnt 기준으로 나열

class SearchSerializer(ModelSerializer):
    """Serializer definition for Search Model."""

    class Meta:
        """Meta definition for RecommendSearchSerializer."""

        model = Search
        fields = ["id", "content"]
        read_only_fields = ["id", "content"]

class UserSearchSerializer(ModelSerializer):
    """Serializer definition for UserSearch Model."""

    search = SearchSerializer(
        # read_only = True,
        required = True,
    )

    class Meta:
        """Meta definition for RecommendSearchSerializer."""

        model = UserSearch
        fields = ["id", "user", "search"]
        read_only_fields = ["id", "cnt", "content"]

class RecommendSearchSerializer(ModelSerializer):
    """Serializer definition for RecommendSearch Model."""

    class Meta:
        """Meta definition for RecommendSearchSerializer."""

        model = RecommendSearch
        fields = ["id", "content"]
        read_only_fields = ["id", "content"]

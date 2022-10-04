from rest_framework.serializers import ModelSerializer

from search.models import RecommendSearch


class RecommendSearchSerializer(ModelSerializer):
    """Serializer definition for RecommendSearch Model."""
    
    # '''Serializer로 전달된 quaryset으로 부터 value만 추출해 리스트로 만들어 리스트를 리턴'''
    # def to_representation(self, instance):
    #     original_data = super().to_representation(instance)
    #     modified_data = [i.values() for i in len(original_data)+1]
    #     return modified_data
    
    class Meta:
        """Meta definition for RecommendSearchSerializer."""

        model = RecommendSearch
        fields = ["content"]
        read_only_fields = ["content"]

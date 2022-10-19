from rest_framework import serializers
from tag.models import Tag

class TagSerializer(serializers.ModelSerializer):
    """Serializer definition for Tag Model."""

    class Meta:
        """Meta definition for TagSerializer."""

        model = Tag
        fields = ["id", "name"]
        read_only_fields = ["id", "name"]

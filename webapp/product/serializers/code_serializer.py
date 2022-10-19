from rest_framework import serializers
from product.models import Code

class CodeSerializer(serializers.ModelSerializer):
    """Serializer definition for Code Model."""

    class Meta:
        """Meta definition for CodeSerializer."""

        model = Code
        fields = ["id", "name"]
        read_only_fields = ["id", "name"]

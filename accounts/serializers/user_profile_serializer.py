from rest_framework import serializers

from accounts.models import User

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer definition for User Model."""

    class Meta:
        """Meta definition for UserProfileSerializer."""

        fields = ["nickname", "username", "introduce", "profile_img"]
        read_only_fields = ["nickname", "username", "introduce", "profile_img"]

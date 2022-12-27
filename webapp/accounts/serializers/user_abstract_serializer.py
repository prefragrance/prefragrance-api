from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserAbstractSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "nickname",
            "age",
            "gender",
            "agree_prefragrance",
            "agree_personal_required",
        ]
        read_only_fields = [
            "id",
            "username",
            "email",
            "agree_prefragrance",
            "agree_personal_required",
        ]

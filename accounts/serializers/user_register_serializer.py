from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers


class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(required=False, max_length=50)
    name = serializers.CharField(required=False, max_length=200)
    age = serializers.IntegerField(required=False)
    gender = serializers.ChoiceField(
        required=False,
        choices=[
            ("M", "Male"),
            ("F", "Female"),
            ("NB", "Non_Binary"),
        ],
    )

    def get_cleaned_data(self):
        data = super().get_cleaned_data()  # username, password, email이 디폴트
        data["nickname"] = self.validated_data.get("nickname", "")
        data["name"] = self.validated_data.get("name", "")
        data["age"] = self.validated_data.get("age", "")
        data["gender"] = self.validated_data.get("gender", "")

        return data

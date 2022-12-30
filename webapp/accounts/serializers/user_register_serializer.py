from accounts.validators import validate_password, validate_username
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class CustomRegisterSerializer(RegisterSerializer):
    username = serializers.CharField(required=True, validators=[validate_username])
    password1 = serializers.CharField(required=True, validators=[validate_password])
    nickname = serializers.CharField(required=True, max_length=50)
    age = serializers.IntegerField(required=False)
    gender = serializers.ChoiceField(
        required=False,
        choices=[
            ("M", "Male"),
            ("F", "Female"),
            ("NB", "Non_Binary"),
        ],
    )
    agree_prefragrance = serializers.BooleanField(label="취향 이용약관 동의 (필수)")
    agree_personal_required = serializers.BooleanField(label="개인정보 수집 및 이용 동의 (필수)")

    def validate(self, data):
        if data["agree_prefragrance"] != True:
            raise serializers.ValidationError(_("이용약관 동의는 필수입니다."))
        elif data["agree_personal_required"] != True:
            raise serializers.ValidationError(_("개인정보 수집 및 이용 동의는 필수입니다."))

        if data["password1"] != data["password2"]:
            raise serializers.ValidationError(_("비밀번호가 일치하지 않습니다."))
        return data

    def get_cleaned_data(self):
        data = super().get_cleaned_data()  # username, password, email이 디폴트
        data["nickname"] = self.validated_data.get("nickname", "")
        data["age"] = self.validated_data.get("age", "")
        data["gender"] = self.validated_data.get("gender", "")
        data["agree_prefragrance"] = self.validated_data.get("agree_prefragrance", "")
        data["agree_personal_required"] = self.validated_data.get(
            "agree_personal_required", ""
        )

        return data

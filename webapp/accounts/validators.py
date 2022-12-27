import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_username(username):
    username_reg = r"^(?=.*[a-z])(?=.*\d)[a-z\d]{6,13}$"
    username_regex = re.compile(username_reg)

    if not username_regex.match(username):
        raise ValidationError("영문+숫자 6자리 이상, 13자리 이하로 아이디 조합되어야합니다.")


def validate_password(password):
    password_reg = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{6,13}$"
    password_regex = re.compile(password_reg)

    if not password_regex.match(password):
        raise ValidationError("영문, 숫자, 특수문자 조합해 6자 이상, 13자 이하 입력해주세요.")

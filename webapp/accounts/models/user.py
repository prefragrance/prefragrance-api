from accounts.validators import validate_username
from django.contrib.auth.models import (AbstractBaseUser, AbstractUser,
                                        BaseUserManager, PermissionsMixin)
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, nickname, username, password=None):
        if not email:
            raise ValueError("must have user email")
        if not nickname:
            raise ValueError("must have user nickname")
        if not username:
            raise ValueError("must have username")
        user = self.model(
            email=self.normalize_email(email), nickname=nickname, username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, username, password=None):
        user = self.create_user(
            email, password=password, nickname=nickname, username=username
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user


def profile_img_upload_path(instance, filename):
    return "profile_img/user_{}/{}".format(instance.username, filename)


class User(AbstractBaseUser, PermissionsMixin):
    """Model definition for User."""

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "nickname", "password"]

    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("NB", "Non_Binary"),
    )

    email = models.EmailField(
        verbose_name=_("email"),
        max_length=200,
        unique=True,
    )
    username = models.CharField(
        verbose_name=_("username"),
        max_length=50,
        unique=True,
        validators=[validate_username],
    )

    nickname = models.CharField(
        max_length=100,
        unique=True,
        error_messages={"unique": "A user with that nickname already exists."},
        null=False,
    )
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)
    profile_img = models.ImageField(
        null=True, blank=True, verbose_name="프로필 이미지", upload_to=profile_img_upload_path
    )
    introduce = models.CharField(
        max_length=300,
        null=True,
        blank=True,
        verbose_name="사용자 소개",
        default="사용자 소개가 없습니다.",
    )
    agree_prefragrance = models.BooleanField(default=False)
    agree_personal_required = models.BooleanField(default=False)

    is_active = models.BooleanField(
        verbose_name=_("Is active"),
        default=True,
    )

    objects = UserManager()

    class Meta:
        """Meta definition for User."""

        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "users"

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_superuser

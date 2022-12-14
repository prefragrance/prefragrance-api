# Generated by Django 4.1 on 2022-12-30 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_remove_user_agree_personal_optional_remove_user_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="agree_personal_required",
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name="user",
            name="agree_prefragrance",
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name="user",
            name="nickname",
            field=models.CharField(
                error_messages={"unique": "A user with that nickname already exists."},
                max_length=100,
                unique=True,
            ),
        ),
    ]

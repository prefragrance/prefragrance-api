# Generated by Django 4.1 on 2022-12-30 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_agree_personal_required_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='agree_personal_required',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='agree_prefragrance',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 4.1 on 2022-11-09 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="rate",
            field=models.FloatField(default=0),
        ),
    ]
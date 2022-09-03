# Generated by Django 4.1 on 2022-09-03 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tag', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=400)),
                ('producer', models.CharField(max_length=400)),
                ('feedback_cnt', models.IntegerField()),
                ('review_cnt', models.IntegerField()),
                ('visit_cnt', models.IntegerField()),
                ('thumbnail_url', models.URLField(blank=True, null=True)),
                ('rate_sum', models.FloatField(blank=True, null=True)),
                ('rate', models.FloatField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cnt', models.IntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tag.tag')),
            ],
        ),
        migrations.CreateModel(
            name='ProductFeedback',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCode',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.code')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='codes',
            field=models.ManyToManyField(related_name='codes', through='product.ProductCode', to='product.code'),
        ),
        migrations.AddField(
            model_name='product',
            name='liked_users',
            field=models.ManyToManyField(related_name='liked_products', through='product.ProductFeedback', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(related_name='product_tags', through='product.ProductTag', to='tag.tag'),
        ),
        migrations.AddConstraint(
            model_name='productfeedback',
            constraint=models.UniqueConstraint(fields=('product', 'user'), name='unique productfeedbacks'),
        ),
    ]

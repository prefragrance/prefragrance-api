

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('tag', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('feedback_cnt', models.IntegerField(default=0)),
                ('review_cnt', models.IntegerField(default=0)),
                ('visit_cnt', models.IntegerField(default=0)),
                ('thumbnail_url', models.URLField(blank=True, null=True)),
                ('rate_sum', models.FloatField(default=0)),
                ('rate', models.FloatField(default=0)),
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
            name='tags',
            field=models.ManyToManyField(related_name='tags', through='product.ProductTag', to='tag.tag'),
            name='liked_users',
            field=models.ManyToManyField(related_name='liked_products', through='product.ProductFeedback', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='productfeedback',
            constraint=models.UniqueConstraint(fields=('product', 'user'), name='unique productfeedbacks'),
        ),
    ]

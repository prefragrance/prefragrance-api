from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('account', '0001_initial'),
        ('tag', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.IntegerField(choices=[(1, 'Spring'), (2, 'Summer'), (3, 'Autumn'), (4, 'Winter')])),
                ('time', models.IntegerField(choices=[(1, 'Day'), (2, 'Night')])),
                ('duration', models.IntegerField(choices=[(1, 'Low'), (2, 'Mid'), (3, 'High')])),
                ('strength', models.IntegerField(choices=[(1, 'Low'), (2, 'Mid'), (3, 'High')])),
                ('content', models.CharField(max_length=1500, verbose_name='내용')),
                ('rate', models.FloatField(validators=[django.core.validators.MinValueValidator(0, 5), django.core.validators.MaxValueValidator(5.0)])),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='날짜')),
                ('feedback_cnt', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Review',
                'db_table': 'review',
            },
        ),
        migrations.CreateModel(
            name='ReviewTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='review.review', verbose_name='리뷰')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tag.tag', verbose_name='키워드')),
            ],
            options={
                'verbose_name': 'Review Tag',
                'verbose_name_plural': 'Review Tag',
                'db_table': 'review_tag',
            },
        ),
        migrations.CreateModel(
            name='ReviewFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='날짜')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='review.review', verbose_name='리뷰')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='사용자')),
            ],
            options={
                'verbose_name': 'Review Feedback',
                'verbose_name_plural': 'Review Feedback',
                'db_table': 'review_feedback',
            },
        ),
        migrations.AddField(
            model_name='review',
            name='liked_users',
            field=models.ManyToManyField(related_name='liked_reviews', through='review.ReviewFeedback', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='product.product', verbose_name='제품'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='사용자'),
        ),
        migrations.AddConstraint(
            model_name='reviewfeedback',
            constraint=models.UniqueConstraint(fields=('user', 'review'), name='unique reviewfeedbacks'),
        ),
    ]

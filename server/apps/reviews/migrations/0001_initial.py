# Generated by Django 4.0.2 on 2024-03-25 13:54

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewVersion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('isfavorite', models.BooleanField(default=False)),
                ('score_1', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('score_2', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('score_3', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('score_4', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('score_5', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('comment', models.TextField(blank=True, null=True)),
                ('comic_version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_version', to='comics.comicversion')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_version', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'バージョンレビュー',
            },
        ),
        migrations.CreateModel(
            name='ReviewMaster',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('isfavorite', models.BooleanField(default=False)),
                ('score_1', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('score_2', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('score_3', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('score_4', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('score_5', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('comment', models.TextField(blank=True, null=True)),
                ('comic_master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_master', to='comics.comicmaster')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_master', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'マスターレビュー',
            },
        ),
        migrations.CreateModel(
            name='ReviewEpisode',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('isfavorite', models.BooleanField(default=False)),
                ('score_1', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('score_2', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('score_3', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('score_4', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('score_5', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('comment', models.TextField(blank=True, null=True)),
                ('comic_episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_episode', to='comics.comicepisode')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_episode', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'エピソードレビュー',
            },
        ),
    ]

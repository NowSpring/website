# Generated by Django 4.0.2 on 2024-03-24 17:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComicMaster',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='タイトル')),
                ('author', models.CharField(max_length=100, verbose_name='作者')),
                ('era', models.CharField(choices=[('1980', '1980'), ('1990', '1990'), ('2000', '2000'), ('2010', '2010')], max_length=100, verbose_name='年代')),
                ('publisher', models.CharField(choices=[('エニックス', 'エニックス'), ('学習研究科', '学習研究科'), ('小学館', '小学館'), ('少年画報社', '少年画報社'), ('徳間書店', '徳間書店'), ('朝日ソラノマ', '朝日ソラノマ'), ('東京三世社', '東京三世社'), ('白泉社', '白泉社'), ('秋田書店', '秋田書店'), ('竹書房', '竹書房'), ('芳文社', '芳文社'), ('角川書店', '角川書店'), ('講談社', '講談社'), ('集英社', '集英社')], max_length=100, verbose_name='出版社')),
                ('target', models.CharField(choices=[('少女', '少女'), ('少年', '少年'), ('女性', '女性'), ('男性', '男性')], max_length=100, verbose_name='対象')),
                ('genre', models.CharField(choices=[('4コマ', '4コマ'), ('SF', 'SF'), ('ギャグ', 'ギャグ'), ('サスペンス', 'サスペンス'), ('スポーツ', 'スポーツ'), ('バトル', 'バトル'), ('ファンタジー', 'ファンタジー'), ('ホラー', 'ホラー'), ('ラブコメ', 'ラブコメ'), ('動物', '動物'), ('恋愛', '恋愛'), ('時代劇', '時代劇')], max_length=100, verbose_name='ジャンル')),
                ('cover', models.ImageField(blank=True, upload_to='cover/master/')),
            ],
            options={
                'verbose_name_plural': 'マスター',
            },
        ),
        migrations.CreateModel(
            name='ComicVersion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('version_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='巻数')),
                ('cover', models.ImageField(blank=True, upload_to='cover/version/')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comics.comicmaster')),
            ],
            options={
                'verbose_name_plural': 'バージョン',
            },
        ),
        migrations.CreateModel(
            name='ComicEpisode',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('episode_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='エピソード数')),
                ('cover', models.ImageField(blank=True, upload_to='cover/episode/')),
                ('pdf', models.FileField(upload_to='pdf/episode/', validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
                ('title_version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comics.comicversion')),
            ],
            options={
                'verbose_name_plural': 'エピソード',
            },
        ),
    ]
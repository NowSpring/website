import uuid
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

from comics.models import ComicMaster, ComicVersion, ComicEpisode


class ReviewBase(models.Model):

    member = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    scoreAlpha = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    scoreBeta = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    scoreCamma = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    scoreDelta = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    scoreEpsilon = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    comment = models.TextField(null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:

        abstract = True  # Django はこのモデルのテーブルを作成しません


class ReviewMaster(ReviewBase):

    comicID = models.ForeignKey(ComicMaster, db_column='comic_id', on_delete=models.CASCADE, related_name='reviewMaster')

    class Meta:

        verbose_name_plural = 'マスターレビュー'

    def __str__(self):

        return f"{self.comicID}"


class ReviewVersion(ReviewBase):

    comicID = models.ForeignKey(ComicVersion, db_column='comic_id', on_delete=models.CASCADE, related_name='reviewVersion')

    class Meta:

        verbose_name_plural = 'バージョンレビュー'

    def __str__(self):

        return f"{self.comicID}"


class ReviewEpisode(ReviewBase):

    comicID = models.ForeignKey(ComicEpisode, db_column='comic_id', on_delete=models.CASCADE, related_name='reviewEpisode')

    class Meta:

        verbose_name_plural = 'エピソードレビュー'

    def __str__(self):

        return f"{self.comicID}"
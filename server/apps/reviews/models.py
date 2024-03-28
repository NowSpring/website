import uuid
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

from comics.models import ComicMaster, ComicVersion, ComicEpisode


class ReviewMaster(models.Model):
    
    member = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviewMaster')
    comicMaster = models.ForeignKey(ComicMaster, on_delete=models.CASCADE, related_name='reviewMaster')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    scoreAlpha = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    scoreBeta = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    scoreCamma = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    scoreDelta = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    scoreEpsilon = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    comment = models.TextField(null=True, blank=True)
    
    class Meta:
      
        verbose_name_plural = 'マスターレビュー'
    
    def __str__(self):
      
        return f"{self.comicMaster}"



class ReviewVersion(models.Model):
    
    member = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviewVersion')
    comicVersion = models.ForeignKey(ComicVersion, on_delete=models.CASCADE, related_name='reviewVersion')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    scoreAlpha = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    scoreBeta = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    scoreCamma = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    scoreDelta = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    scoreEpsilon = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    comment = models.TextField(null=True, blank=True)
    
    class Meta:
      
        verbose_name_plural = 'バージョンレビュー'
    
    def __str__(self):
      
        return f"{self.comicVersion}"


class ReviewEpisode(models.Model):
    
    member = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviewEpisode')
    comicEpisode = models.ForeignKey(ComicEpisode, on_delete=models.CASCADE, related_name='reviewEpisode')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    scoreAlpha = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    scoreBeta = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    scoreCamma = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    scoreDelta = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    scoreEpsilon = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    comment = models.TextField(null=True, blank=True)
    
    class Meta:
      
        verbose_name_plural = 'エピソードレビュー'
    
    def __str__(self):
      
        return f"{self.comicEpisode}"
import uuid
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

from comics.models import ComicMaster, ComicVersion, ComicEpisode


class ReviewMaster(models.Model):
    
    member = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='review_master')
    comic_master = models.ForeignKey(ComicMaster, on_delete=models.CASCADE, related_name='review_master')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    score_1 = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    score_2 = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    score_3 = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    score_4 = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    score_5 = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    comment = models.TextField(null=True, blank=True)
    
    class Meta:
      
        verbose_name_plural = 'マスターレビュー'
    
    def __str__(self):
      
        return f"Review by {self.member} on {self.comic_master}"



class ReviewVersion(models.Model):
    
    member = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='review_version')
    comic_version = models.ForeignKey(ComicVersion, on_delete=models.CASCADE, related_name='reviews_version')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    score_1 = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    score_2 = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    score_3 = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    score_4 = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    score_5 = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    comment = models.TextField(null=True, blank=True)
    
    class Meta:
      
        verbose_name_plural = 'バージョンレビュー'
    
    def __str__(self):
      
        return f"Review by {self.member} on {self.comic_version}"


class ReviewEpisode(models.Model):
    
    member = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='review_episode')
    comic_episode = models.ForeignKey(ComicEpisode, on_delete=models.CASCADE, related_name='review_episode')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    score_1 = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    score_2 = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    score_3 = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    score_4 = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    score_5 = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    comment = models.TextField(null=True, blank=True)
    
    class Meta:
      
        verbose_name_plural = 'エピソードレビュー'
    
    def __str__(self):
      
        return f"Review by {self.member} on {self.comic_episode}"
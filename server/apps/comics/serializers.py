from rest_framework import serializers

from comics.models import ComicMaster, ComicVersion, ComicEpisode
from reviews.models import ReviewMaster, ReviewVersion, ReviewEpisode
from reviews.serializers import ReviewMasterSerializer, ReviewVersionSerializer, ReviewEpisodeSerializer


class ComicMasterSerializer(serializers.ModelSerializer):

  representation = serializers.SerializerMethodField()
  review = serializers.SerializerMethodField()

  class Meta:

    model = ComicMaster
    fields = ['id', 'title', 'author', 'era', 'publisher', 'target', 'genre', 'cover', 'representation', 'review']

  def get_representation(self, obj):

    return str(obj)

  def get_review(self, obj):

    member_id = self.context.get('request').query_params.get('member_id')
    reviews = ReviewMaster.objects.filter(comicID=obj, member_id=member_id)
    review = reviews.first()

    if review is not None:

      return ReviewMasterSerializer(review).data

    else:

      return None


class ComicVersionSerializer(serializers.ModelSerializer):

  representation = serializers.SerializerMethodField()
  review = serializers.SerializerMethodField()

  class Meta:

    model = ComicVersion
    fields = ["id", "version", "cover", "title_id", 'representation', 'review']

  def get_representation(self, obj):

    return str(obj)

  def get_review(self, obj):

    member_id = self.context.get('request').query_params.get('member_id')
    reviews = ReviewVersion.objects.filter(comicID=obj, member_id=member_id)
    review = reviews.first()

    if review is not None:

        return ReviewVersionSerializer(review).data

    else:

        return None


class ComicEpisodeSerializer(serializers.ModelSerializer):

  representation = serializers.SerializerMethodField()
  review = serializers.SerializerMethodField()

  class Meta:

    model = ComicEpisode
    fields = ["id", "episode", "cover", "include_id", 'representation', 'review']

  def get_representation(self, obj):

    return str(obj)

  def get_review(self, obj):

    member_id = self.context.get('request').query_params.get('member_id')
    reviews = ReviewEpisode.objects.filter(comicID=obj, member_id=member_id)
    review = reviews.first()

    if review is not None:

        return ReviewEpisodeSerializer(review).data

    else:

        return None
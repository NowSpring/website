from rest_framework import serializers

from comics.models import ComicMaster, ComicVersion, ComicEpisode


class StrRepresentationMixin:

    str_representation = serializers.SerializerMethodField()

    def get_str_representation(self, obj):
        return str(obj)


class ComicMasterSerializer(StrRepresentationMixin, serializers.ModelSerializer):

  class Meta:

    model = ComicMaster
    fields = "__all__"


class ComicVersionSerializer(StrRepresentationMixin, serializers.ModelSerializer):

  class Meta:

    model = ComicVersion
    fields = "__all__"

class ComicEpisodeSerializer(StrRepresentationMixin, serializers.ModelSerializer):

  class Meta:

    model = ComicEpisode
    fields = "__all__"
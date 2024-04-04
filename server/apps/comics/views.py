from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from comics.models import ComicMaster, ComicVersion, ComicEpisode
from comics.serializers import ComicMasterSerializer, ComicVersionSerializer, ComicEpisodeSerializer
from comics.filters import ComicVersionFilter, ComicEpisodeFilter

class ComicMasterViewSet(viewsets.ModelViewSet):

  queryset = ComicMaster.objects.all()
  serializer_class = ComicMasterSerializer

  def get_serializer_context(self):

    context = super(ComicMasterViewSet, self).get_serializer_context()
    context.update({"request": self.request})

    return context

  def get_queryset(self):

    queryset = ComicMaster.objects.all()
    exclude_id = self.request.query_params.get('exclude_id', None)

    if exclude_id is not None:

      queryset = queryset.exclude(id=exclude_id)

    return queryset


class ComicVersionViewSet(viewsets.ModelViewSet):

  queryset = ComicVersion.objects.all()
  serializer_class = ComicVersionSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_class = ComicVersionFilter

  def get_queryset(self):

    queryset = ComicVersion.objects.all()
    exclude_id = self.request.query_params.get('exclude_id', None)

    if exclude_id is not None:

      queryset = queryset.exclude(id=exclude_id)

    return queryset


class ComicEpisodeViewSet(viewsets.ModelViewSet):

  queryset = ComicEpisode.objects.all()
  serializer_class = ComicEpisodeSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_class = ComicEpisodeFilter

  def get_queryset(self):

    queryset = ComicEpisode.objects.all()
    exclude_id = self.request.query_params.get('exclude_id', None)

    if exclude_id is not None:

      queryset = queryset.exclude(id=exclude_id)

    return queryset

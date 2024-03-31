from rest_framework import viewsets

from reviews.models import ReviewMaster, ReviewVersion, ReviewEpisode
from reviews.serializers import ReviewMasterSerializer, ReviewVersionSerializer, ReviewEpisodeSerializer


class BaseReviewViewSet(viewsets.ModelViewSet):

  def get_queryset(self):

    queryset = super().get_queryset()
    member_id = self.request.query_params.get('member_id', None)

    if member_id is not None:

      queryset = queryset.filter(member=member_id)

    return queryset


class ReviewMasterViewSet(BaseReviewViewSet):

    queryset = ReviewMaster.objects.all()
    serializer_class = ReviewMasterSerializer


class ReviewVersionViewSet(BaseReviewViewSet):

    queryset = ReviewVersion.objects.all()
    serializer_class = ReviewVersionSerializer


class ReviewEpisodeViewSet(BaseReviewViewSet):

    queryset = ReviewEpisode.objects.all()
    serializer_class = ReviewEpisodeSerializer
from rest_framework import routers

from apps.members.views import MemberViewSet
from apps.comics.views import ComicMasterViewSet, ComicVersionViewSet, ComicEpisodeViewSet

router = routers.DefaultRouter()
router.register('member', MemberViewSet)
router.register('comic/master', ComicMasterViewSet)
router.register('comic/version', ComicVersionViewSet)
router.register('comic/episode', ComicEpisodeViewSet)
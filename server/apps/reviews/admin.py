from django.contrib import admin

from reviews.models import ReviewMaster, ReviewVersion, ReviewEpisode

# 共通の設定を持つベースクラス
class ReviewAdminBaseConfig(admin.ModelAdmin):

    search_fields = ('member__username', 'comicID', 'scoreAlpha', 'scoreBeta', 'scoreCamma', 'scoreDelta', 'scoreEpsilon',)
    list_filter = ('member', 'comicID', 'scoreAlpha', 'scoreBeta', 'scoreCamma', 'scoreDelta', 'scoreEpsilon',)
    list_display = ('member', 'comicID', 'scoreAlpha', 'scoreBeta', 'scoreCamma', 'scoreDelta', 'scoreEpsilon',)
    ordering = ('member', 'comicID',)
    fieldsets = (
        (None, {'fields': ('member', 'comicID', 'scoreAlpha', 'scoreBeta', 'scoreCamma', 'scoreDelta', 'scoreEpsilon', 'comment')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('member', 'comicID', 'scoreAlpha', 'scoreBeta', 'scoreCamma', 'scoreDelta', 'scoreEpsilon', 'comment')}
         ),
    )

# 各モデルのadmin設定
class ReviewMasterAdminConfig(ReviewAdminBaseConfig):

    model = ReviewMaster

class ReviewVersionAdminConfig(ReviewAdminBaseConfig):

    model = ReviewVersion

class ReviewEpisodeAdminConfig(ReviewAdminBaseConfig):

    model = ReviewEpisode



admin.site.register(ReviewMaster, ReviewMasterAdminConfig)
admin.site.register(ReviewVersion, ReviewVersionAdminConfig)
admin.site.register(ReviewEpisode, ReviewEpisodeAdminConfig)
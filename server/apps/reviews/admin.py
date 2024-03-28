from django.contrib import admin

from reviews.models import ReviewMaster, ReviewVersion, ReviewEpisode

class ReviewMasterAdminConfig(admin.ModelAdmin):
  
    model = ReviewMaster
    search_fields = ('member', 'comicMaster', 'scoreAlpha', 'scoreBeta', 'scoreCamma', 'scoreDelta', 'scoreEpsilon',)
    list_filter = ('member', 'comicMaster', 'scoreAlpha', 'scoreBeta', 'scoreCamma', 'scoreDelta', 'scoreEpsilon',)
    list_display = ('member', 'comicMaster', 'scoreAlpha', 'scoreBeta', 'scoreCamma', 'scoreDelta', 'scoreEpsilon',)
    ordering = ('member', 'comicMaster',)
    fieldsets = (
        (None, {'fields': ('member', 'comicMaster', 'scoreAlpha', 'scoreBeta', 'scoreCamma', 'scoreDelta', 'scoreEpsilon', 'comment')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('member', 'comicMaster', 'scoreAlpha', 'scoreBeta', 'scoreCamma', 'scoreDelta', 'scoreEpsilon', 'comment')}
         ),
    )
    

class ReviewVersionAdminConfig(admin.ModelAdmin):
  
    model = ReviewVersion
    search_fields = ('member', 'comicVersion', 'scoreAlpha', 'scoreBeta', 'scoreCamma', 'scoreDelta', 'scoreEpsilon',)
    list_filter = ('member', 'comicVersion', 'scoreAlpha', 'scoreBeta', 'scoreCamma', 'scoreDelta', 'scoreEpsilon',)
    list_display = ('member', 'comicVersion', 'scoreAlpha', 'scoreBeta', 'scoreCamma', 'scoreDelta', 'scoreEpsilon',)
    ordering = ('member', 'comicVersion',)
    fieldsets = (
        (None, {'fields': ('member', 'comicVersion', 'scoreAlpha', 'scoreBeta', 'scoreCamma', 'scoreDelta', 'scoreEpsilon', 'comment')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('member', 'comicVersion', 'scoreAlpha', 'scoreBeta', 'scoreCamma', 'scoreDelta', 'scoreEpsilon', 'comment')}
         ),
    )


class ReviewEpisodeAdminConfig(admin.ModelAdmin):
  
    model = ReviewEpisode
    search_fields = ('member', 'comicEpisode', 'scoreAlpha', 'scoreBeta', 'scoreCamma', 'scoreDelta', 'scoreEpsilon',)
    list_filter = ('member', 'comicEpisode', 'scoreAlpha', 'scoreBeta', 'scoreCamma', 'scoreDelta', 'scoreEpsilon',)
    list_display = ('member', 'comicEpisode', 'scoreAlpha', 'scoreBeta', 'scoreCamma', 'scoreDelta', 'scoreEpsilon',)
    ordering = ('member', 'comicEpisode',)
    fieldsets = (
        (None, {'fields': ('member', 'comicEpisode', 'scoreAlpha', 'scoreBeta', 'scoreCamma', 'scoreDelta', 'scoreEpsilon', 'comment')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('member', 'comicEpisode', 'scoreAlpha', 'scoreBeta', 'scoreCamma', 'scoreDelta', 'scoreEpsilon', 'comment')}
         ),
    )



admin.site.register(ReviewMaster, ReviewMasterAdminConfig)
admin.site.register(ReviewVersion, ReviewVersionAdminConfig)
admin.site.register(ReviewEpisode, ReviewEpisodeAdminConfig)
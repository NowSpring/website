from django.contrib import admin

from comics.models import ComicMaster, ComicVersion, ComicEpisode

class ComicMasterAdminConfig(admin.ModelAdmin):

    model = ComicMaster
    search_fields = ('title', 'author', 'era', 'publisher', 'target', 'genre',)
    list_filter = ('title', 'author', 'era', 'publisher', 'target', 'genre',)
    ordering = ('title',)
    list_display = ('id', 'title', 'author', 'era', 'publisher', 'target', 'genre',)
    fieldsets = (
        (None, {'fields': ('title', 'author', 'era', 'publisher', 'target', 'genre', 'cover', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('title', 'author', 'era', 'publisher', 'target', 'genre', 'cover', )}
         ),
    )


class ComicVersionAdminConfig(admin.ModelAdmin):

    model = ComicVersion
    search_fields = ('title', 'version',)
    list_filter = ('title', 'version',)
    ordering = ('title', 'version',)
    list_display = ('id', 'title', 'version',)
    fieldsets = (
        (None, {'fields': ('title', 'version', 'cover',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('title', 'version', 'cover',)}
         ),
    )


class ComicEpisodeAdminConfig(admin.ModelAdmin):

    model = ComicEpisode
    search_fields = ('include', 'episode',)
    list_filter = ('include', 'episode',)
    ordering = ('include', 'episode',)
    list_display = ('id', 'include', 'episode',)
    fieldsets = (
        (None, {'fields': ('include', 'episode', 'cover', 'pdf',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('include', 'episode', 'cover', 'pdf',)}
         ),
    )


admin.site.register(ComicMaster, ComicMasterAdminConfig)
admin.site.register(ComicVersion, ComicVersionAdminConfig)
admin.site.register(ComicEpisode, ComicEpisodeAdminConfig)
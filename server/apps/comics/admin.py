from django.contrib import admin

from comics.models import ComicMaster, ComicVersion, ComicEpisode

class ComicMasterAdminConfig(admin.ModelAdmin):
  
    model = ComicMaster
    search_fields = ('title', 'author', 'era', 'publisher', 'target', 'genre',)
    list_filter = ('title', 'author', 'era', 'publisher', 'target', 'genre',)
    ordering = ('title',)
    list_display = ('title', 'author', 'era', 'publisher', 'target', 'genre',)
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
    list_display = ('title', 'version',)
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
    search_fields = ('title', 'version', 'episode',)
    list_filter = ('title', 'version', 'episode',)
    ordering = ('title', 'version', 'episode',)
    list_display = ('title', 'version', 'episode',)
    fieldsets = (
        (None, {'fields': ('title', 'version', 'episode', 'cover', 'pdf',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('title', 'version', 'episode', 'cover', 'pdf',)}
         ),
    )


admin.site.register(ComicMaster, ComicMasterAdminConfig)
admin.site.register(ComicVersion, ComicVersionAdminConfig)
admin.site.register(ComicEpisode, ComicEpisodeAdminConfig)
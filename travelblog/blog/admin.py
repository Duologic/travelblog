from __future__ import unicode_literals

from adminsortable.admin import NonSortableParentAdmin, SortableStackedInline
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

from django.contrib import admin

from .models import Article, Comment, Location, Photo


class PhotoAdminInline(SortableStackedInline):
    model = Photo
    extra = 1
    prepopulated_fields = {'slug': ('title',)}


class ArticleAdmin(NonSortableParentAdmin):
    inlines = [PhotoAdminInline]
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'summary', 'article',)
    list_display = ('title', 'location', 'published', 'draft',)
    list_filter = ('location', 'published', 'draft',)

admin.site.register(Article, ArticleAdmin)


class LocationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    list_display = ('name', 'address', 'geolocation',)
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }

admin.site.register(Location, LocationAdmin)


class CommentAdmin(admin.ModelAdmin):
    search_fields = ('name', 'mail', 'comment',)
    list_display = ('name', 'mail', 'get_article_title', 'created', 'hidden',)
    list_filter = ('article__title', 'created', 'hidden', 'mail',)

    def get_article_title(self, obj):
        if obj.article:
            return obj.article.title
        return None
    get_article_title.short_description = 'Article'

admin.site.register(Comment, CommentAdmin)

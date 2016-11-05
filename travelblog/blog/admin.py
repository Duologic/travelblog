from __future__ import unicode_literals

from adminsortable.admin import NonSortableParentAdmin, SortableStackedInline
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

admin.site.register(Article, ArticleAdmin)


class LocationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

admin.site.register(Location, LocationAdmin)


class CommentAdmin(admin.ModelAdmin):
    search_fields = ('name', 'mail', 'comment',)

admin.site.register(Comment, CommentAdmin)

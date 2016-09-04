from __future__ import unicode_literals

from adminsortable.admin import NonSortableParentAdmin, SortableStackedInline
from django.contrib import admin

from .models import Photo, Article


class PhotoAdminInline(SortableStackedInline):
    model = Photo
    extra = 1


class ArticleAdmin(NonSortableParentAdmin):
    inlines = [PhotoAdminInline]

admin.site.register(Article, ArticleAdmin)

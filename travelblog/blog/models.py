from __future__ import unicode_literals

from adminsortable.models import SortableMixin
from django_google_maps import fields as map_fields

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

import os


class Location(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    location = models.ForeignKey(Location)
    published = models.DateTimeField(help_text='Date after which this should be published')
    draft = models.BooleanField(help_text='Mark as draft, ignore published date')
    summary = models.TextField(help_text='Short summary, may contain HTML')
    article = models.TextField(help_text='Actual article, also may contain HTML')

    def __str__(self):
        return '{0} published on {1}'.format(self.title, self.published)


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    mail = models.EmailField(max_length=200)
    article = models.ForeignKey(Article, blank=True, null=True, on_delete=models.SET_NULL)
    comment = models.TextField()
    hidden = models.BooleanField(default=False, help_text='Hide this comment without removing')

    def __str__(self):
        return '{0} commented on {1}'.format(self.name, self.comment)


class Photo(SortableMixin):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    location = models.ForeignKey(Location, blank=True, null=True, on_delete=models.SET_NULL)
    article = models.ForeignKey(Article, blank=True, null=True, on_delete=models.SET_NULL)
    photo = models.ImageField(upload_to=os.path.join(settings.MEDIA_ROOT, 'photos'))
    display_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    hidden = models.BooleanField(default=False, help_text='Hide this photo without removing')

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return 'Photo #{0}'.format(self.display_order)

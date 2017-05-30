# coding=utf-8

from __future__ import unicode_literals

import mimetypes
from django.core.exceptions import ValidationError

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class VideoValidator(object):

    error_messages = {
        'content_type': _("File of type %(content_type)s are not supported.")
    }

    def __init__(self, content_types=()):
        self.content_types = content_types

    def __call__(self, data):
        guessed_mimetype, guessed_enc = mimetypes.guess_type(data.name)
        if self.content_types and guessed_mimetype not in self.content_types:
            raise ValidationError(
                self.error_messages['content_type'],
                code='content_type',
                params={'content_type': guessed_mimetype}
            )


class Video(models.Model):

    STATUS_CHOICES = (
        ('loading', _('Loading')),
        ('loaded', _('Loaded')),
        ('queued', _('Queued')),
        ('processing', _('Processing')),
        ('ready', _('Ready')),
        ('error', _('Error')),
    )

    id = models.CharField(
        max_length=50, primary_key=True, verbose_name=_('id')
    )
    category = models.ForeignKey(Category, verbose_name=_('Category'))
    duration = models.CharField(
        max_length=50, blank=True, null=True, verbose_name=_('Duration')
    )
    preview = models.ImageField(
        blank=True, null=True, verbose_name=_('Preview')
    )
    status = models.CharField(
        max_length=30, choices=STATUS_CHOICES, null=True, blank=True,
        verbose_name=_('Status')
    )
    video_validator = VideoValidator(content_types=['video/mp4', 'video/avi'])
    video = models.FileField(
        verbose_name=_('Video'), validators=[video_validator]
    )

# coding=utf-8

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


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
    video = models.FileField(verbose_name=_('Video'))

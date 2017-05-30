# coding=utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Video(models.Model):

    STATUS_CHOICES = (
        ('loading', _(u'Loading')),
        ('loaded', _(u'Loaded')),
        ('queued', _(u'Queued')),
        ('processing', _(u'Processing')),
        ('ready', _(u'Ready')),
        ('error', _(u'Error')),
    )

    id = models.CharField(max_length=50, primary_key=True)
    category = models.ForeignKey(Category)
    duration = models.CharField(max_length=50, blank=True, null=True)
    preview = models.ImageField(blank=True, null=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES,
                              null=True, blank=True)
    video = models.FileField()

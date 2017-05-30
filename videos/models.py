# coding=utf-8

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Video(models.Model):

    STATUS_CHOICES = (
        ('loading', u'Загружается'),
        ('loaded', u'Загружен'),
        ('queued', u'В очереди'),
        ('processing', u'Обрабатывается'),
        ('ready', u'Готово'),
        ('error', u'Ошибка'),
    )

    id = models.CharField(max_length=50, primary_key=True)
    category = models.ForeignKey(Category)
    duration = models.CharField(max_length=50, blank=True, null=True)
    preview = models.ImageField(blank=True, null=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES,
                              null=True, blank=True)
    video = models.FileField()

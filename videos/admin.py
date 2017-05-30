# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Category, Video


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'video')

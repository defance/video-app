# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .forms import NewVideoForm
from .models import Video


class NewVideoView(CreateView):
    template_name = "videos/new_video.html"
    form_class = NewVideoForm
    model = Video
    success_url = reverse_lazy('home')

    def form_valid(self, form):

        # Create convert task

        return super(NewVideoView, self).form_valid(form)


class VideosListView(ListView):
    model = Video
    context_object_name = "video_list"


__all__ = ['NewVideoView']

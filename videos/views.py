# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView

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


__all__ = ['NewVideoView']

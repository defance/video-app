# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from uuid import uuid4

from .forms import NewVideoForm
from .models import Video


class NewVideoView(CreateView):
    template_name = "videos/new_video.html"
    form_class = NewVideoForm
    model = Video
    success_url = reverse_lazy('home')

    def __init__(self, **kwargs):
        super(NewVideoView, self).__init__(**kwargs)
        self.random_id = str(uuid4())

    def form_valid(self, form):

        # Create convert task

        return super(NewVideoView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        # Do we need it here?
        context = super(NewVideoView, self).get_context_data(**kwargs)
        context['random_id'] = self.random_id
        return context

    def get_form_kwargs(self):
        kw = super(NewVideoView, self).get_form_kwargs()
        kw['random_id'] = self.random_id
        return kw


class VideosListView(ListView):
    model = Video
    context_object_name = "video_list"


__all__ = ['NewVideoView']

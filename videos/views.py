# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.urls import reverse

from .forms import NewVideoForm


class NewVideoView(FormView):
    template_name = "videos/new_video.html"
    form_class = NewVideoForm

    def form_valid(self, form):
        form.video_upload()
        return redirect(reverse('home'))


__all__ = ['NewVideoView']

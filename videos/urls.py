from __future__ import unicode_literals

from django.conf.urls import url
from videos.views import VideosListView

from .views import NewVideoView

urlpatterns = [
    url(r'^all/$', VideosListView.as_view(), name='all_videos'),
    url(r'^$', NewVideoView.as_view(), name='home'),
]

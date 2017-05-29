from __future__ import unicode_literals

from django.conf.urls import url

from .views import NewVideoView

urlpatterns = [
    url(r'^$', NewVideoView.as_view(), name='home'),
]

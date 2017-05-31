from __future__ import unicode_literals

from factory import SubFactory, Sequence
from factory.django import DjangoModelFactory

from ..models import Category, Video


class CategoryFactory(DjangoModelFactory):

    class Meta(object):
        model = Category


class VideoFactory(DjangoModelFactory):

    class Meta(object):
        model = Video

    id = Sequence('{}'.format)
    category = SubFactory(CategoryFactory)

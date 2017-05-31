from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.utils import IntegrityError
from django.test import TestCase, TransactionTestCase
from factory.django import FileField
from mock import Mock

from .factories import CategoryFactory, VideoFactory
from ..models import Category, VideoValidator, Video


class TestCategory(TestCase):

    def test_unicode(self):
        category = Category(name='Test category')
        self.assertEqual(unicode(category), category.name)

    def test_ok(self):
        c1 = Category.objects.create(name='Test')
        c2 = Category.objects.get(name='Test')
        self.assertIsInstance(c1, Category)
        self.assertIsInstance(c2, Category)
        self.assertEqual(c1, c2)

    def test_empty_name(self):
        # useless in sqlite
        pass

    def test_long_name(self):
        # useless in sqlite
        pass


class TestVideoValidator(TestCase):

    def setUp(self):
        self.empty_validator = VideoValidator()
        self.validator = VideoValidator(['video/mp4', 'video/x-msvideo'])

    def test_init_empty(self):
        self.assertEqual((), self.empty_validator.content_types)
        self.assertNotIn('video/mp4', self.empty_validator.content_types)

    def test_init_non_empty(self):
        self.assertIn('video/mp4', self.validator.content_types)
        self.assertNotIn('video/png', self.validator.content_types)

    def test_validation_error(self):
        mock_file = Mock()
        mock_file.name = 'image.png'
        self.assertRaises(ValidationError, self.validator, mock_file)

    def test_validation_ok(self):
        mock_file = Mock()
        mock_file.name = 'video.avi'
        self.assertIsNone(self.validator(mock_file))


class TestVideo(TransactionTestCase):

    def setUp(self):
        self.category = CategoryFactory.create(name='Test category')
        self.video = VideoFactory.create(category=self.category)

    def test_video_validation_ok(self):
        mp4_file = FileField(filename='file.mp4')
        video = VideoFactory.create(video=mp4_file)
        self.assertIsNone(video.clean_fields())

    def test_video_fail_validation(self):
        # No category set
        mp4_file = FileField(filename='file.mp4')
        with self.assertRaisesRegex(IntegrityError, 'videos_video.category_id'):
            VideoFactory.create(video=mp4_file, category=None)

        # Error in video file
        png_file = FileField(filename='file.png')
        video = VideoFactory.create(video=png_file)
        with self.assertRaises(ValidationError) as cm:
            video.clean_fields()
        # self.assertEqual('content_type', cm.exception.code)

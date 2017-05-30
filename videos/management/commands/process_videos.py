from __future__ import unicode_literals

from django.core.management.base import BaseCommand
from django.utils import translation
from django.utils.translation import ugettext_lazy as _

from ...utils import process_videos


class Command(BaseCommand):
    help = _('Process all videos being in queued state.')

    def handle(self, *args, **options):

        # Enable translation for this one.
        # See: https://code.djangoproject.com/ticket/10078
        from django.conf import settings
        translation.activate(settings.LANGUAGE_CODE)

        result = process_videos(process=True)

        self.stdout.write(_('Job finished.'))
        self.stdout.write(
            _('  * Successfully processed videos: %(successful)s') %
            {'successful': result[True]}
        )
        self.stdout.write(
            _('  * Failed to process videos: %(failed)s') %
            {'failed': result[False]}
        )

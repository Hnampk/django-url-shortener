from django.core.management.base import BaseCommand, CommandError

from shortener.models import KirrURL


class Command(BaseCommand):
    help = 'Refresh the shortcode of all the urls'

    def handle(self, *args, **options):
        KirrURL.objects.refresh_shortcodes()

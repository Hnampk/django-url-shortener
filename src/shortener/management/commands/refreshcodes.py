from django.core.management.base import BaseCommand, CommandError

from shortener.models import KirrURL

class Command(BaseCommand):
    help = 'Refresh the shortcode of all the'

    def add_arguments(self, parser):
        # parser.add_argument('items', type=int) # "must have" value
        parser.add_argument('--items', type=int) # optional items value with --

    def handle(self, *args, **options):
        KirrURL.objects.refresh_shortcodes(items=options['items'])
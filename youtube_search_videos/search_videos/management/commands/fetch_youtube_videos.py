from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Fetch the vidoes from youtube.'

    def handle(self, *args, **options):
        pass

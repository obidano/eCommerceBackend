from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'FAIRE MES TEST DJANGO'

    def handle(self, *args, **options):
        print('BIENVENU DANS LE BROUILLON')

from django.core.management import BaseCommand
from guests.models import Party, Guest


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        count = Guest.objects.count()
        choice = input(f'Really delete all {count} guests?! (y/n): ')
        if choice.strip().lower() == 'y':
            Party.objects.all().delete()
            print('Guests deleted')
        else:
            print('Cancelled')

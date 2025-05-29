from django.core.management.base import BaseCommand
from recepty.models import Recept, Kuchar, Kategorie

class Command(BaseCommand):
    help = 'Vymaže všechna data z databáze'

    def handle(self, *args, **kwargs):
        self.stdout.write('Mažu všechny recepty...')
        Recept.objects.all().delete()
        
        self.stdout.write('Mažu všechny kuchaře...')
        Kuchar.objects.all().delete()
        
        self.stdout.write('Mažu všechny kategorie...')
        Kategorie.objects.all().delete()
        
        self.stdout.write(self.style.SUCCESS('Databáze byla úspěšně vyčištěna.'))
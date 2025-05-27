from django.core.management.base import BaseCommand
from recepty.models import Recept, Kuchar, Kategorie
from django.core.files import File
import os

class Command(BaseCommand):
    help = 'Přidá ukázkové recepty do databáze'

    def handle(self, *args, **kwargs):
        # Vytvoření kategorií
        kategorie1, _ = Kategorie.objects.get_or_create(nazev='Hlavní jídla')
        kategorie2, _ = Kategorie.objects.get_or_create(nazev='Polévky')
        kategorie3, _ = Kategorie.objects.get_or_create(nazev='Dezerty')

        # Vytvoření kuchařů
        kuchar1, _ = Kuchar.objects.get_or_create(jmeno='Jan Novák', bio='Profesionální kuchař')
        kuchar2, _ = Kuchar.objects.get_or_create(jmeno='Marie Svobodová', bio='Domácí kuchařka')

        # Přidání dalších autorů
        kuchar3, _ = Kuchar.objects.get_or_create(jmeno='Petr Dvořák', bio='Milovník tradiční české kuchyně.')
        kuchar4, _ = Kuchar.objects.get_or_create(jmeno='Eva Novotná', bio='Specialistka na sladké dezerty.')
        kuchar5, _ = Kuchar.objects.get_or_create(jmeno='Tomáš Král', bio='Experimentátor a moderní kuchař.')

        # Cesty k obrázkům (všechny obrázky musí být ve složce media/recepty/)
        images = {
            'Svíčková na smetaně': 'svickova.jpg',
            'Guláš': 'gulas.jpg',
            'Česnečka': 'cesnecka.jpg',
            'Kuřecí řízek': 'rizek.jpg',
            'Štrúdl': 'strudl.jpg',
        }

        # Vytvoření receptů
        recepty = [
            {
                'nazev': 'Svíčková na smetaně',
                'popis': 'Tradiční české jídlo s knedlíkem a brusinkami.',
                'kategorie': kategorie1,
                'kuchar': kuchar1,
                'obrazek': images['Svíčková na smetaně']
            },
            {
                'nazev': 'Guláš',
                'popis': 'Vydatný hovězí guláš s chlebem.',
                'kategorie': kategorie1,
                'kuchar': kuchar1,
                'obrazek': images['Guláš']
            },
            {
                'nazev': 'Česnečka',
                'popis': 'Oblíbená polévka s česnekem a sýrem.',
                'kategorie': kategorie2,
                'kuchar': kuchar2,
                'obrazek': images['Česnečka']
            },
            {
                'nazev': 'Kuřecí řízek',
                'popis': 'Křupavý kuřecí řízek s bramborovou kaší.',
                'kategorie': kategorie1,
                'kuchar': kuchar2,
                'obrazek': images['Kuřecí řízek']
            },
            {
                'nazev': 'Štrúdl',
                'popis': 'Jablečný štrúdl s vanilkovou zmrzlinou.',
                'kategorie': kategorie3,
                'kuchar': kuchar2,
                'obrazek': images['Štrúdl']
            }
        ]

        # Přidání dalších receptů
        recepty += [
            {
                'nazev': 'Rajská omáčka',
                'popis': 'Oblíbená rajská omáčka s hovězím masem a houskovým knedlíkem.',
                'kategorie': kategorie1,
                'kuchar': kuchar3,
                'obrazek': 'rajska.jpg',
            },
            {
                'nazev': 'Bramboračka',
                'popis': 'Tradiční česká polévka s houbami a bramborami.',
                'kategorie': kategorie2,
                'kuchar': kuchar3,
                'obrazek': 'bramboracka.jpg',
            },
            {
                'nazev': 'Tiramisu',
                'popis': 'Italský dezert s mascarpone, kávou a piškoty.',
                'kategorie': kategorie3,
                'kuchar': kuchar4,
                'obrazek': 'tiramisu.jpg',
            },
            {
                'nazev': 'Kuřecí kari',
                'popis': 'Exotické kuřecí kari s kokosovým mlékem a rýží.',
                'kategorie': kategorie1,
                'kuchar': kuchar5,
                'obrazek': 'kurecikari.jpg',
            },
            {
                'nazev': 'Čokoládový dort',
                'popis': 'Nadýchaný čokoládový dort s polevou.',
                'kategorie': kategorie3,
                'kuchar': kuchar4,
                'obrazek': 'dort.jpg',
            },
            {
                'nazev': 'Houbová polévka',
                'popis': 'Krémová polévka z čerstvých hub.',
                'kategorie': kategorie2,
                'kuchar': kuchar5,
                'obrazek': 'houbova-polevka.jpg',
            },
        ]

        for recept_data in recepty:
            obrazek_name = recept_data.pop('obrazek')
            recept, created = Recept.objects.get_or_create(**recept_data)
            # Nastav obrázek pouze pokud není nastaven
            if obrazek_name:
                relative_path = f"recepty/{obrazek_name}"
                # Pokud obrázek není nastaven nebo je jiný, nastav ho
                if not recept.obrazek or recept.obrazek.name != relative_path:
                    recept.obrazek.name = relative_path
                    recept.save()

        self.stdout.write(self.style.SUCCESS('Ukázkové recepty byly úspěšně přidány do databáze.'))


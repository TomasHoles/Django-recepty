from django.core.management.base import BaseCommand
from recepty.models import Recept, Kuchar, Kategorie
from django.core.files import File
import os
import json

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
            'Tiramisu': 'tiramisu.jpg',
            'Bramboračka': 'bramboracka.jpg',
            'Čokoládový dort': 'dort.jpg',
            'Houbová polévka': 'houbova-polevka.jpg',
        }

        # Vytvoření receptů - omezeno na 9 receptů
        recepty = [
            {
                'nazev': 'Svíčková na smetaně',
                'popis': 'Tradiční české jídlo s knedlíkem a brusinkami.',
                'kategorie': kategorie1,
                'kuchar': kuchar1,
                'obrazek': images['Svíčková na smetaně'],
                'ingredience': ['800 g hovězí svíčkové', '150 g kořenové zeleniny (mrkev, celer, petržel)', 
                               '2 cibule', '100 g slaniny', '250 ml smetany ke šlehání', '2 lžíce octa', 
                               '2 lžíce cukru', '2 bobkové listy, nové koření, pepř, sůl', 'olej, máslo'],
                'postup': ['Maso prošpikujte slaninou, osolte a opepřete.', 
                          'Opečte na oleji, přidejte zeleninu a cibuli, restujte.', 
                          'Přidejte koření, podlijte vodou, duste doměkka.', 
                          'Maso vyjměte, zeleninu rozmixujte, přidejte smetanu, dochuťte octem a cukrem.', 
                          'Podávejte s houskovým knedlíkem a brusinkami.']
            },
            {
                'nazev': 'Guláš',
                'popis': 'Vydatný hovězí guláš s chlebem.',
                'kategorie': kategorie1,
                'kuchar': kuchar1,
                'obrazek': images['Guláš'],
                'ingredience': ['800 g hovězí kližky', '2 cibule', '3 stroužky česneku', '2 lžíce sladké papriky', 
                               '1 lžíce majoránky', '1 lžíce rajčatového protlaku', 'sůl, pepř, sádlo'],
                'postup': ['Cibuli osmahněte na sádle, přidejte maso a opečte.', 
                          'Přidejte česnek, papriku, protlak, zalijte vodou.', 
                          'Osolte, opepřete, duste doměkka.', 
                          'Dochutťe majoránkou, podávejte s chlebem.']
            },
            {
                'nazev': 'Česnečka',
                'popis': 'Oblíbená polévka s česnekem a sýrem.',
                'kategorie': kategorie2,
                'kuchar': kuchar2,
                'obrazek': images['Česnečka'],
                'ingredience': ['6 stroužků česneku', '4 brambory', '1 l zeleninového vývaru', 
                               'majoránka, sůl, pepř', 'chleba na krutony, sýr na posypání'],
                'postup': ['Brambory nakrájejte na kostičky, uvařte ve vývaru.', 
                          'Přidejte prolisovaný česnek, dochuťte.', 
                          'Přidejte krutony a sýr až na talíři.']
            },
            {
                'nazev': 'Kuřecí řízek',
                'popis': 'Křupavý kuřecí řízek s bramborovou kaší.',
                'kategorie': kategorie1,
                'kuchar': kuchar2,
                'obrazek': images['Kuřecí řízek'],
                'ingredience': ['4 kuřecí prsa', 'hladká mouka, vejce, strouhanka', 
                               'sůl, pepř, olej na smažení', 'bramborová kaše na podávání'],
                'postup': ['Maso naklepejte, osolte, opepřete.', 
                          'Obalte v mouce, vejci a strouhance.', 
                          'Osmažte dozlatova na oleji.', 
                          'Podávejte s bramborovou kaší.']
            },
            {
                'nazev': 'Štrúdl',
                'popis': 'Jablečný štrúdl s vanilkovou zmrzlinou.',
                'kategorie': kategorie3,
                'kuchar': kuchar2,
                'obrazek': images['Štrúdl'],
                'ingredience': ['1 balení listového těsta', '4 jablka', 'rozinky, skořice, cukr', 
                               'vejce na potření', 'vanilková zmrzlina na podávání'],
                'postup': ['Jablka oloupejte, nastrouhejte, smíchejte s cukrem, skořicí a rozinkami.', 
                          'Těsto rozválejte, naplňte jablky, zaviňte.', 
                          'Potřete vejcem, pečte dozlatova.', 
                          'Podávejte s vanilkovou zmrzlinou.']
            },
            {
                'nazev': 'Bramboračka',
                'popis': 'Tradiční česká polévka s houbami a bramborami.',
                'kategorie': kategorie2,
                'kuchar': kuchar3,
                'obrazek': images['Bramboračka'],
                'ingredience': ['500 g brambor', '100 g hub', '2 mrkve', '1 celer', '1 petržel', 
                               '3 stroužky česneku', 'majoránka, sůl, pepř', '2 lžíce másla', '1,5 l vývaru'],
                'postup': ['Zeleninu očistěte a nakrájejte na kostičky.', 
                          'Na másle orestujte zeleninu, přidejte houby.', 
                          'Zalijte vývarem, přidejte brambory nakrájené na kostky.', 
                          'Vařte doměkka, přidejte česnek a majoránku, dochuťte.']
            },
            {
                'nazev': 'Tiramisu',
                'popis': 'Italský dezert s mascarpone, kávou a piškoty.',
                'kategorie': kategorie3,
                'kuchar': kuchar4,
                'obrazek': images['Tiramisu'],
                'ingredience': ['500 g mascarpone', '4 vejce', '100 g cukru', '200 g cukrářských piškotů', 
                               '300 ml silné kávy', '2 lžíce rumu', 'kakao na posypání'],
                'postup': ['Oddělte žloutky od bílků. Žloutky vyšlehejte s cukrem do pěny.', 
                          'Vmíchejte mascarpone. Z bílků ušlehejte tuhý sníh a opatrně vmíchejte do krému.', 
                          'Piškoty namáčejte v kávě s rumem a vrstvěte s krémem do formy.', 
                          'Navrch dejte vrstvu krému, posypte kakaem a nechte v lednici ztuhnout.']
            },
            {
                'nazev': 'Čokoládový dort',
                'popis': 'Nadýchaný čokoládový dort s polevou.',
                'kategorie': kategorie3,
                'kuchar': kuchar4,
                'obrazek': images['Čokoládový dort'],
                'ingredience': ['200 g hořké čokolády', '200 g másla', '4 vejce', '150 g cukru', 
                               '100 g hladké mouky', '1 lžička prášku do pečiva', '100 ml mléka', 
                               'čokoládová poleva na ozdobu'],
                'postup': ['Čokoládu s máslem rozpusťte ve vodní lázni.', 
                          'Vejce vyšlehejte s cukrem do pěny, přidejte čokoládovou směs.', 
                          'Vmíchejte mouku s práškem do pečiva a mléko.', 
                          'Pečte při 180°C asi 35 minut, po vychladnutí ozdobte polevou.']
            },
            {
                'nazev': 'Houbová polévka',
                'popis': 'Krémová polévka z čerstvých hub.',
                'kategorie': kategorie2,
                'kuchar': kuchar5,
                'obrazek': images['Houbová polévka'],
                'ingredience': ['300 g čerstvých hub', '2 brambory', '1 mrkev', '1 celer', '1 petržel', 
                               '200 ml smetany', '2 lžíce másla', 'sůl, pepř', '1 l zeleninového vývaru'],
                'postup': ['Houby očistěte a nakrájejte na plátky.', 
                          'Zeleninu očistěte a nakrájejte na kostičky.', 
                          'Na másle orestujte zeleninu, přidejte houby a krátce orestujte.', 
                          'Zalijte vývarem, vařte doměkka, přidejte smetanu a rozmixujte.']
            },
        ]

        # Nejprve odstraníme všechny existující recepty
        Recept.objects.all().delete()
        
        # Poté přidáme nové recepty
        for index, recept_data in enumerate(recepty, start=1):
            # Uložíme si ingredience a postup před odstraněním z recept_data
            ingredience = recept_data.pop('ingredience', [])
            postup = recept_data.pop('postup', [])
            obrazek_name = recept_data.pop('obrazek')
            
            # Přidáme číslo receptu do názvu
            recept_data['nazev'] = f"{index}. {recept_data['nazev']}"
            
            recept, created = Recept.objects.get_or_create(**recept_data)
            
            # Uložíme ingredience a postup jako JSON
            recept.ingredience = json.dumps(ingredience)
            recept.postup = json.dumps(postup)
            
            # Nastav obrázek pouze pokud není nastaven
            if obrazek_name:
                relative_path = f"recepty/{obrazek_name}"
                # Pokud obrázek není nastaven nebo je jiný, nastav ho
                if not recept.obrazek or recept.obrazek.name != relative_path:
                    recept.obrazek.name = relative_path
            
            recept.save()

        self.stdout.write(self.style.SUCCESS('Ukázkové recepty byly úspěšně přidány do databáze (celkem 9 receptů).'))


# Tento soubor definuje strukturu databáze pro aplikaci receptů

from django.db import models

class Kategorie(models.Model):
    """Model pro kategorie receptů (např. Hlavní jídla, Polévky, Dezerty).
    Každý recept musí patřit do jedné kategorie."""
    nazev = models.CharField(max_length=100)  # Název kategorie, např. 'Hlavní jídla'

    def __str__(self):
        return self.nazev

class Kuchar(models.Model):
    """Model pro autory receptů.
    Obsahuje základní informace o autorovi a jeho biografii."""
    jmeno = models.CharField(max_length=100)  # Jméno autora receptu
    bio = models.TextField(blank=True)  # Biografie autora, nepovinné

    def __str__(self):
        return self.jmeno

class Recept(models.Model):
    """Hlavní model pro recepty.
    Obsahuje všechny informace o receptu včetně ingrediencí a postupu přípravy."""
    nazev = models.CharField(max_length=200)  # Název receptu
    popis = models.TextField()  # Krátký popis receptu
    obrazek = models.ImageField(upload_to='recepty/', blank=True, null=True)  # Obrázek receptu (nepovinný)
    kategorie = models.ForeignKey(Kategorie, on_delete=models.CASCADE)  # Vazba na kategorii
    kuchar = models.ForeignKey(Kuchar, on_delete=models.CASCADE)  # Vazba na autora
    datum_vytvoreni = models.DateTimeField(auto_now_add=True)  # Datum přidání receptu
    ingredience = models.TextField(default='[]')  # JSON seznam ingrediencí
    postup = models.TextField(default='[]')  # JSON seznam kroků postupu

    def __str__(self):
        return self.nazev

    @property
    def ingredience_list(self):
        """Vrací seznam ingrediencí jako Python list."""
        import json
        return json.loads(self.ingredience)

    @property
    def postup_list(self):
        """Vrací seznam kroků postupu jako Python list."""
        import json
        return json.loads(self.postup)

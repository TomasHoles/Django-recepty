from django.db import models
from django.core.validators import MinLengthValidator

class Kategorie(models.Model):
    nazev = models.CharField(
        max_length=100,
        unique=True,
        validators=[MinLengthValidator(3)],
        help_text="Název kategorie, např. 'Hlavní jídla'"
    )

    class Meta:
        verbose_name = 'Kategorie'
        verbose_name_plural = 'Kategorie'
        ordering = ['nazev']

    def __str__(self):
        return self.nazev

class Kuchar(models.Model):
    jmeno = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)],
        help_text="Jméno autora receptu"
    )
    bio = models.TextField(
        blank=True,
        help_text="Biografie autora"
    )

    class Meta:
        verbose_name = 'Kuchař'
        verbose_name_plural = 'Kuchaři'
        ordering = ['jmeno']

    def __str__(self):
        return self.jmeno

class Recept(models.Model):
    OBTIZNOST_CHOICES = [
        ('L', 'Lehká'),
        ('S', 'Střední'),
        ('T', 'Těžká')
    ]

    nazev = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(5)],
        help_text="Název receptu"
    )
    popis = models.TextField(
        validators=[MinLengthValidator(20)],
        help_text="Krátký popis receptu"
    )
    obrazek = models.ImageField(
        upload_to='recepty/',
        blank=True,
        null=True,
        help_text="Obrázek receptu"
    )
    kategorie = models.ForeignKey(
        Kategorie,
        on_delete=models.CASCADE,
        related_name='recepty',
        help_text="Kategorie receptu"
    )
    kuchar = models.ForeignKey(
        Kuchar,
        on_delete=models.CASCADE,
        related_name='recepty',
        help_text="Autor receptu"
    )
    datum_vytvoreni = models.DateTimeField(
        auto_now_add=True,
        help_text="Datum přidání receptu"
    )
    cas_pripravy = models.PositiveIntegerField(
        default=30,
        help_text="Čas přípravy v minutách"
    )
    obtiznost = models.CharField(
        max_length=1,
        choices=OBTIZNOST_CHOICES,
        default='S',
        help_text="Obtížnost receptu"
    )
    ingredience = models.TextField(
        default='[]',
        help_text="JSON seznam ingrediencí"
    )
    postup = models.TextField(
        default='[]',
        help_text="JSON seznam kroků postupu"
    )

    class Meta:
        verbose_name = 'Recept'
        verbose_name_plural = 'Recepty'
        ordering = ['id']  # Seřadí vzestupně podle ID

    def __str__(self):
        return self.nazev

    @property
    def ingredience_list(self):
        import json
        return json.loads(self.ingredience)

    @property
    def postup_list(self):
        import json
        return json.loads(self.postup)

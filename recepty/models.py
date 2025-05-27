from django.db import models

# Create your models here.

class Kategorie(models.Model):
    nazev = models.CharField(max_length=100)

    def __str__(self):
        return self.nazev

class Kuchar(models.Model):
    jmeno = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.jmeno

class Recept(models.Model):
    nazev = models.CharField(max_length=200)
    popis = models.TextField()
    obrazek = models.ImageField(upload_to='recepty/', blank=True, null=True)
    kategorie = models.ForeignKey(Kategorie, on_delete=models.CASCADE)
    kuchar = models.ForeignKey(Kuchar, on_delete=models.CASCADE)
    datum_vytvoreni = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nazev

# Generated by Django 5.0.2 on 2025-05-20 08:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Kuchar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jmeno', models.CharField(max_length=100)),
                ('bio', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(max_length=200)),
                ('popis', models.TextField()),
                ('obrazek', models.ImageField(blank=True, null=True, upload_to='recepty/')),
                ('datum_vytvoreni', models.DateTimeField(auto_now_add=True)),
                ('kategorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recepty.kategorie')),
                ('kuchar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recepty.kuchar')),
            ],
        ),
    ]

# Generated by Django 5.2.1 on 2025-05-29 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recepty', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recept',
            name='ingredience',
            field=models.TextField(default='[]'),
        ),
        migrations.AddField(
            model_name='recept',
            name='postup',
            field=models.TextField(default='[]'),
        ),
    ]

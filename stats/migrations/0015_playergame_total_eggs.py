# Generated by Django 4.0.6 on 2022-07-26 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0014_playergame_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='playergame',
            name='total_eggs',
            field=models.IntegerField(default=0, verbose_name="Nombre d'oeuf"),
        ),
    ]

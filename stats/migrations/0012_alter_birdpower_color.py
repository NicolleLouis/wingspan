# Generated by Django 4.0.6 on 2022-07-16 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0011_alter_birdcard_nest_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birdpower',
            name='color',
            field=models.CharField(choices=[('WHITE', 'Blanc'), ('BROWN', 'Marron'), ('PINK', 'Rose'), ('BLUE', 'Bleu'), ('NOTHING', 'Pas de couleur')], default=None, max_length=13),
        ),
    ]

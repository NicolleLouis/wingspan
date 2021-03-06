# Generated by Django 4.0.6 on 2022-07-30 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0022_alter_bird_bird_card_alter_birdcard_bird_power_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('habitat', models.CharField(blank=True, choices=[('FOREST', 'Forêt'), ('PLAIN', 'Plaine'), ('SWAMP', 'Marais')], default=None, max_length=6, null=True)),
                ('engine_size', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]

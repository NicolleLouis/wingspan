# Generated by Django 4.0.6 on 2022-07-13 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BirdCard',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=24, null=True)),
                ('points', models.IntegerField(default=0)),
                ('can_live_in_forest', models.BooleanField(default=False)),
                ('can_live_in_swamp', models.BooleanField(default=False)),
                ('can_live_in_plain', models.BooleanField(default=False)),
                ('price', models.IntegerField(default=1, verbose_name='Prix (En nourriture)')),
                ('egg_number', models.IntegerField(default=1, verbose_name='Nombre d"oeuf maximal')),
                ('nest_type', models.CharField(choices=[('BONUS', 'Bonus'), ('BOWL', 'Nid'), ('CAVITY', 'Tronc'), ('GROUND', 'A même le sol'), ('PLATFORM', 'Plateforme')], default=None, max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='BirdPower',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=24, null=True)),
                ('color', models.CharField(choices=[('WHITE', 'Blanc'), ('BROWN', 'Marron'), ('PINK', 'Rose'), ('BLUE', 'Bleu')], default=None, max_length=13)),
                ('type', models.CharField(choices=[('HUNT', 'Chasse'), ('FOOD', 'Nourriture'), ('REPRODUCTION', 'Reproduction'), ('EGG', 'Oeuf'), ('CARD_DRAW', 'Pioche'), ('CARD_BONUS', 'Piocher des carte bonus'), ('HATCH_BIRD', 'Poser un autre oiseau'), ('MOVING', 'Déplacement'), ('OTHER', 'Autre')], default=None, max_length=13)),
                ('is_collaborative', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=24, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerGame',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bonus_point', models.IntegerField(default=0, verbose_name='Point des cartes bonus')),
                ('round_point', models.IntegerField(default=0, verbose_name='Point des fin de manches')),
                ('card_kept_at_beginning', models.IntegerField(default=3, verbose_name='Nombre de carte gardées en début de partie')),
                ('card_at_the_end', models.IntegerField(default=0, verbose_name='Nombre de cartes restantes en fin de partie')),
                ('food_at_the_end', models.IntegerField(default=3, verbose_name='Nombre de nourritures restantes en fin de partie')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_games', to='stats.game')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='stats.user')),
            ],
        ),
        migrations.CreateModel(
            name='Bird',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('habitat', models.CharField(choices=[('FOREST', 'Forêt'), ('PLAIN', 'Plaine'), ('SWAMP', 'Marais')], default=None, max_length=6)),
                ('food_stored', models.IntegerField(default=None, null=True, verbose_name='Nourritures Stockées')),
                ('cards_stored', models.IntegerField(default=None, null=True, verbose_name='Cartes Stockées')),
                ('eggs_hatched', models.IntegerField(default=None, null=True, verbose_name='Oeuf Stockés')),
                ('position_in_habitat', models.IntegerField(default=0, verbose_name='Position dans l"habitat')),
                ('bird_card', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stats.birdcard')),
                ('player_game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='birds', to='stats.playergame')),
            ],
        ),
    ]

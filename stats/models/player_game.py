from django.db import models
from django.contrib import admin

from stats.models.bird import BirdInline


class PlayerGame(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        'User',
        on_delete=models.PROTECT,
        null=True,
    )
    game = models.ForeignKey(
        'Game',
        on_delete=models.CASCADE,
        null=False,
        related_name='player_games'
    )
    bonus_point = models.IntegerField(
        default=0,
        null=False,
        verbose_name='Point des cartes bonus'
    )
    round_point = models.IntegerField(
        default=0,
        null=False,
        verbose_name='Point des fin de manches'
    )
    card_kept_at_beginning = models.IntegerField(
        default=3,
        null=False,
        verbose_name='Nombre de carte gardées en début de partie'
    )
    card_at_the_end = models.IntegerField(
        default=0,
        null=False,
        verbose_name='Nombre de cartes restantes en fin de partie'
    )
    food_at_the_end = models.IntegerField(
        default=3,
        null=False,
        verbose_name='Nombre de nourritures restantes en fin de partie'
    )

    def __str__(self):
        return f'{self.game}: {self.user}'


@admin.register(PlayerGame)
class PlayerGameAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'game',
        'bonus_point',
        'round_point',
    )

    inlines = (
        BirdInline,
    )


class PlayerGameInline(admin.TabularInline):
    model = PlayerGame

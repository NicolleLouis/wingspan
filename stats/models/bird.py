from django.db import models
from django.contrib import admin

from stats.constants.habitat import Habitat


class Bird(models.Model):
    id = models.AutoField(primary_key=True)
    bird_card = models.ForeignKey(
        'BirdCard',
        on_delete=models.PROTECT,
        null=False,
    )
    player_game = models.ForeignKey(
        'PlayerGame',
        on_delete=models.CASCADE,
        null=False,
        related_name='birds'
    )
    habitat = models.CharField(
        max_length=6,
        choices=Habitat.choices,
        default=None,
    )
    food_stored = models.IntegerField(
        null=True,
        default=0,
        verbose_name='Nourritures Stockées'
    )
    cards_stored = models.IntegerField(
        null=True,
        default=0,
        verbose_name='Cartes Stockées'
    )
    position_in_habitat = models.IntegerField(
        null=False,
        default=0,
        verbose_name='Position dans l"habitat'
    )

    def __str__(self):
        return f'{self.bird_card.name} in {self.habitat}'


@admin.register(Bird)
class BirdAdmin(admin.ModelAdmin):
    list_display = (
        'bird_card',
        'habitat',
        'food_stored',
        'cards_stored',
        'position_in_habitat',
    )

    autocomplete_fields = (
        'bird_card',
    )


class BirdInline(admin.TabularInline):
    model = Bird

    extra = 0

    autocomplete_fields = (
        'bird_card',
    )

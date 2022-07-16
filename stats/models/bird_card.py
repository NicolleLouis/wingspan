from django.db import models
from django.contrib import admin

from stats.constants.nest import Nest


class BirdCard(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        null=True,
        max_length=50
    )
    points = models.IntegerField(
        null=False,
        default=0,
    )
    can_live_in_forest = models.BooleanField(
        default=False
    )
    can_live_in_plain = models.BooleanField(
        default=False
    )
    can_live_in_swamp = models.BooleanField(
        default=False
    )
    price = models.IntegerField(
        null=False,
        default=1,
        verbose_name='Prix (En nourriture)'
    )
    egg_number = models.IntegerField(
        null=False,
        default=1,
        verbose_name='Nombre d"oeuf maximal'
    )
    nest_type = models.CharField(
        max_length=13,
        choices=Nest.choices,
        default=None,
    )
    bird_power = models.ForeignKey(
        'BirdPower',
        on_delete=models.PROTECT,
        null=True,
    )

    def __str__(self):
        return self.name


@admin.register(BirdCard)
class BirdCardAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'points',
        'nest_type',
        'egg_number',
    )

    search_fields = (
        'name',
    )

    ordering = ['name']

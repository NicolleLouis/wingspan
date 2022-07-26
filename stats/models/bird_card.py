from django.db import models
from django.contrib import admin

from stats.constants.extension import Extension
from stats.constants.nest import Nest


class BirdCard(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        null=True,
        max_length=100
    )
    english_name = models.CharField(
        null=True,
        max_length=100
    )
    latin_name = models.CharField(
        null=True,
        max_length=100
    )
    extension = models.CharField(
        max_length=13,
        choices=Extension.choices,
        default=Extension.CORE,
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
        null=True,
    )
    bird_power = models.ForeignKey(
        'BirdPower',
        on_delete=models.PROTECT,
        null=True,
    )

    def __str__(self):
        if self.name is not None:
            return self.name
        return self.latin_name


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
        'latin_name',
    )

    ordering = ['name']

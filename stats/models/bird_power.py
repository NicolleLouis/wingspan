from django.db import models
from django.contrib import admin

from stats.constants.color import Color
from stats.constants.power_type import PowerType


class BirdPower(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        null=True,
        max_length=24
    )
    color = models.CharField(
        max_length=13,
        choices=Color.choices,
        default=None,
    )
    type = models.CharField(
        max_length=13,
        choices=PowerType.choices,
        default=None,
    )
    is_collaborative = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f"{self.color} {self.type} {self.name}"


@admin.register(BirdPower)
class BirdPowerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'color',
        'type',
        'is_collaborative',
    )

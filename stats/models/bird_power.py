from django.db import models
from django.contrib import admin

from stats.constants.color import Color
from stats.constants.power_type import PowerType


class BirdPower(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        null=True,
        max_length=100
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
        null=True
    )
    is_collaborative = models.BooleanField(
        default=False
    )

    def __str__(self):
        if self.type is not None:
            color = getattr(Color, f'{self.color}_HUMAN')
            type = getattr(PowerType, f'{self.type}_HUMAN')
            return f"{color} - {type} - {self.name}"
        else:
            return 'None'


@admin.register(BirdPower)
class BirdPowerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'color',
        'type',
        'is_collaborative',
    )

    ordering = [
        'color',
        'type',
        'name',
    ]

    def has_delete_permission(self, request, obj=None):
        return False

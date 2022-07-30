from django.db import models
from django.contrib import admin

from stats.constants.habitat import Habitat


class Engine(models.Model):
    id = models.AutoField(primary_key=True)
    habitat = models.CharField(
        max_length=6,
        choices=Habitat.choices,
        default=None,
        null=True,
        blank=True
    )
    engine_size = models.IntegerField(
        default=0,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.habitat}: {self.engine_size}'


@admin.register(Engine)
class EngineAdmin(admin.ModelAdmin):
    list_display = (
        'habitat',
        'engine_size',
    )

    def has_delete_permission(self, request, obj=None):
        return False

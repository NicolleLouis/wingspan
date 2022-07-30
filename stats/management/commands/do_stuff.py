from django.core.management.base import BaseCommand

from stats.models import Game


class Command(BaseCommand):
    def handle(self, *args, **options):
        player_game = Game.objects.filter(winner=None)
        player_game.delete()

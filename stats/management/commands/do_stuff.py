from django.core.management.base import BaseCommand

from stats.models import PlayerGame
from stats.service.player_game_service import PlayerGameService


class Command(BaseCommand):
    def handle(self, *args, **options):
        player_game = PlayerGame.objects.all()[0]
        print(player_game)
        PlayerGameService.get_score(player_game)

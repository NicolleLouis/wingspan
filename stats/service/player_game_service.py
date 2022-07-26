from __future__ import annotations

from typing import TYPE_CHECKING

from stats.service.bird_card_service import BirdService

if TYPE_CHECKING:
    from stats.models import PlayerGame


class PlayerGameService:
    @staticmethod
    def compute_score(player_game: PlayerGame) -> None:
        score = player_game.bonus_point + player_game.round_point + player_game.total_eggs
        for bird in player_game.birds.all():
            score += BirdService.get_score(bird)
        player_game.score = score
        player_game.save()

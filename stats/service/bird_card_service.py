from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from stats.models import Bird, PlayerGame


class BirdService:
    @staticmethod
    def get_score(bird: Bird) -> int:
        score = bird.bird_card.points + bird.cards_stored + bird.food_stored
        return score

    @staticmethod
    def update_bird_info(
            bird: Bird,
            player_game: PlayerGame,
            habitat: str,
            position_in_habitat: int
    ):
        bird.player_game = player_game
        bird.habitat = habitat
        bird.position_in_habitat = position_in_habitat
        bird.save()

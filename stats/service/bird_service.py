from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from stats.models import Bird, PlayerGame


class BirdService:
    def __init__(self, bird: Bird):
        self.bird = bird

    def get_score(self) -> int:
        bird = self.bird
        score = bird.bird_card.points + bird.cards_stored + bird.food_stored
        return score

    def update_bird_info(
            self,
            player_game: PlayerGame,
            habitat: str,
            position_in_habitat: int
    ):
        bird = self.bird
        bird.player_game = player_game
        bird.habitat = habitat
        bird.position_in_habitat = position_in_habitat
        bird.save()

    def get_power_color(self):
        from stats.service.bird_card_service import BirdCardService

        return BirdCardService(self.bird.bird_card).get_power_color()

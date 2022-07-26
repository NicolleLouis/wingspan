from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from stats.models import Bird


class BirdService:
    @staticmethod
    def get_score(bird: Bird) -> int:
        score = bird.bird_card.points + bird.cards_stored + bird.food_stored
        return score

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from stats.models import BirdCard


class BirdCardService:
    def __init__(self, bird_card: BirdCard):
        self.bird_card = bird_card

    def get_power_color(self):
        return self.bird_card.bird_power.color

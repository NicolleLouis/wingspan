from __future__ import annotations
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from stats.models import Game


class GameService:
    @staticmethod
    def get_player_name(game: Game) -> str:
        player_names = list(
            map(
                lambda player: player.name,
                game.players()
            )
        )
        return ', '.join(player_names)

from __future__ import annotations

import pdb
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from stats.models import PlayerGame


class PlayerGameService:
    @staticmethod
    def get_score(player_game: PlayerGame) -> int:
       pdb.set_trace()

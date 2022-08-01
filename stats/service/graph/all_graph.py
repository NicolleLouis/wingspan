from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from stats.service.graph.engine_score import EngineGraphService
from stats.service.graph.score_bird_number import BirdNumberGraphService
from stats.service.graph.score_bird_number_habitat import BirdNumberHabitatGraphService

if TYPE_CHECKING:
    from stats.models import PlayerGame


class AllGraph:
    graph_list = [
        EngineGraphService,
        BirdNumberGraphService,
        BirdNumberHabitatGraphService,
    ]

    def __init__(
            self,
            display: bool = False,
            player_games: Optional[List[PlayerGame]] = None
    ):
        from stats.repositories.player_games import PlayerGameRepository

        self.display = display
        if player_games is None:
            self.player_games = PlayerGameRepository.all()
        else:
            self.player_games = player_games

        self.result()

    def result(self):
        for graph in self.graph_list:
            graph(display=self.display, player_games=self.player_games)

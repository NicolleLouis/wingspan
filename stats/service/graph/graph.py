from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional
import matplotlib.pyplot as plt

if TYPE_CHECKING:
    from stats.models import PlayerGame


class GraphService:
    filename = None

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
        self.fig, self.ax = plt.subplots()

        self.compute_data()
        self.add_options()
        self.result()

    @staticmethod
    def add_options():
        raise NotImplemented

    def result(self):
        if self.filename is None:
            raise Exception('Define a filename to save graph')
        plt.savefig(self.filename)
        if self.display:
            plt.show()

    def compute_data(self):
        raise NotImplemented

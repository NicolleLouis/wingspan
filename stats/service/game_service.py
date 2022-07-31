from __future__ import annotations
from typing import TYPE_CHECKING

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

    @staticmethod
    def compute_winner(game: Game) -> None:
        from stats.service.player_game.player_game import PlayerGameService

        for player_game in game.player_games.all():
            PlayerGameService(player_game).compute_data()

        winner = max(
            game.player_games.all(),
            key=lambda player_game: player_game.score
        )
        game.winner = winner
        game.save()

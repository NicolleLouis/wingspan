from __future__ import annotations

from typing import TYPE_CHECKING

from stats.constants.habitat import Habitat
from stats.service.bird_service import BirdService

if TYPE_CHECKING:
    from stats.models import PlayerGame, Bird


class PlayerGameService:
    def __init__(self, player_game: PlayerGame):
        self.player_game = player_game

    def compute_data(self) -> None:
        from stats.service.player_game.engine import EngineService

        self.update_birds_info()
        self.compute_score()
        EngineService(self.player_game).compute_engine()

    def compute_score(self) -> None:
        player_game = self.player_game
        score = player_game.bonus_point + player_game.round_point + player_game.total_eggs
        for bird in player_game.birds.all():
            score += BirdService(bird).get_score()
        player_game.score = score
        player_game.save()

    def update_bird_info(self, bird: Bird, habitat: str, position_in_habitat: int) -> None:
        if bird is not None:
            BirdService(bird).update_bird_info(
                self.player_game, habitat, position_in_habitat
            )

    def update_birds_info(self) -> None:
        player_game = self.player_game
        self.update_bird_info(
            player_game.forest_1, Habitat.FOREST, 1
        )
        self.update_bird_info(
            player_game.forest_2, Habitat.FOREST, 2
        )
        self.update_bird_info(
            player_game.forest_3, Habitat.FOREST, 3
        )
        self.update_bird_info(
            player_game.forest_4, Habitat.FOREST, 4
        )
        self.update_bird_info(
            player_game.forest_5, Habitat.FOREST, 5
        )
        self.update_bird_info(
            player_game.plain_1, Habitat.PLAIN, 1
        )
        self.update_bird_info(
            player_game.plain_2, Habitat.PLAIN, 2
        )
        self.update_bird_info(
            player_game.plain_3, Habitat.PLAIN, 3
        )
        self.update_bird_info(
            player_game.plain_4, Habitat.PLAIN, 4
        )
        self.update_bird_info(
            player_game.plain_5, Habitat.PLAIN, 5
        )
        self.update_bird_info(
            player_game.swamp_1, Habitat.SWAMP, 1
        )
        self.update_bird_info(
            player_game.swamp_2, Habitat.SWAMP, 2
        )
        self.update_bird_info(
            player_game.swamp_3, Habitat.SWAMP, 3
        )
        self.update_bird_info(
            player_game.swamp_4, Habitat.SWAMP, 4
        )
        self.update_bird_info(
            player_game.swamp_5, Habitat.SWAMP, 5
        )

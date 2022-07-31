from __future__ import annotations

from typing import TYPE_CHECKING

from stats.constants.color import Color
from stats.constants.habitat import Habitat
from stats.service.bird_service import BirdService

if TYPE_CHECKING:
    from stats.models import PlayerGame, Engine


class EngineService:
    def __init__(self, player_game: PlayerGame):
        self.player_game = player_game
        self.forest_repartition: Repartition
        self.plain_repartition: Repartition
        self.swamp_repartition: Repartition

    def compute_engine(self) -> None:
        self.compute_repartition()
        engine = self.compute_best_engine()
        self.player_game.engine = engine
        self.player_game.save()

    def compute_best_engine(self) -> (Habitat, int):
        forest_engine_size = self.forest_repartition.browns
        forest_engine_size += self.forest_repartition.all
        forest_engine_size += self.plain_repartition.others
        forest_engine_size += self.swamp_repartition.others

        plain_engine_size = self.plain_repartition.browns
        plain_engine_size += self.plain_repartition.all
        plain_engine_size += self.forest_repartition.others
        plain_engine_size += self.swamp_repartition.others

        swamp_engine_size = self.swamp_repartition.browns
        swamp_engine_size += self.swamp_repartition.all
        swamp_engine_size += self.forest_repartition.others
        swamp_engine_size += self.plain_repartition.others

        if forest_engine_size >= max(plain_engine_size, swamp_engine_size):
            return self.create_engine(Habitat.FOREST, forest_engine_size)
        if plain_engine_size >= max(forest_engine_size, swamp_engine_size):
            return self.create_engine(Habitat.PLAIN, plain_engine_size)
        if swamp_engine_size >= max(plain_engine_size, forest_engine_size):
            return self.create_engine(Habitat.SWAMP, swamp_engine_size)

    def compute_repartition(self) -> None:
        self.forest_repartition = self.compute_habitat_power_color_repartition(Habitat.FOREST)
        self.plain_repartition = self.compute_habitat_power_color_repartition(Habitat.PLAIN)
        self.swamp_repartition = self.compute_habitat_power_color_repartition(Habitat.SWAMP)

    def compute_habitat_power_color_repartition(self, habitat) -> Repartition:
        browns = 0
        others = 0
        birds = self.player_game.birds.filter(habitat=habitat)
        for bird in birds:
            color = BirdService(bird).get_power_color()
            if color == Color.BROWN:
                browns += 1
            elif color in [Color.BLUE, Color.PINK, Color.WHITE]:
                others += 1
        return Repartition(browns, others, len(birds))

    @staticmethod
    def create_engine(habitat: Habitat, engine_size: int) -> Engine:
        from stats.models.engine import Engine

        return Engine.objects.create(
            habitat=habitat,
            engine_size=engine_size
        )


class Repartition:
    def __init__(self, browns: int, others: int, all: int):
        self.browns = browns
        self.others = others
        self.all = all

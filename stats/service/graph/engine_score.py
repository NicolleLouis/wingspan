import matplotlib.pyplot as plt

from stats.constants.habitat import Habitat
from stats.service.graph.graph import GraphService


class EngineGraphService(GraphService):
    filename = 'stats/files/graph/engine.jpg'

    def add_options(self):
        plt.ylabel('Score')
        plt.xlabel('Taille du moteur')
        plt.legend(loc='upper left')
        plt.title('Score/Taille du moteur')

    def compute_data(self):
        forest_engines = self.player_games.filter(engine__habitat=Habitat.FOREST)
        self.draw_games(forest_engines, 'green', 'Forêt')
        plain_engines = self.player_games.filter(engine__habitat=Habitat.PLAIN)
        self.draw_games(plain_engines, 'gold', 'Plaine')
        swamp_engines = self.player_games.filter(engine__habitat=Habitat.SWAMP)
        self.draw_games(swamp_engines, 'blue', 'Marais')

    def draw_games(self, player_games, color, label):
        scores = []
        engine_sizes = []
        for player_game in player_games:
            scores.append(player_game.score)
            engine_sizes.append(player_game.engine.engine_size)
        self.ax.scatter(engine_sizes, scores, color=color, label=label)

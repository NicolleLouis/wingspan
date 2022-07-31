import matplotlib.pyplot as plt

from stats.constants.habitat import Habitat


class EngineGraphService:
    filename = 'stats/files/graph/engine.jpg'

    def __init__(self, display: bool):
        from stats.repositories.player_games import PlayerGameRepository

        self.display = display
        self.player_games = PlayerGameRepository.all()
        self.fig, self.ax = plt.subplots()

        self.compute_data()
        self.add_options()
        self.result()

    def add_options(self):
        plt.xlabel('Score')
        plt.ylabel('Taille du moteur')
        plt.legend(loc='upper left')
        plt.title('Score/Taille du moteur')

    def result(self):
        plt.savefig(self.filename)
        if self.display:
            plt.show()

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
        self.ax.scatter(scores, engine_sizes, color=color, label=label)

import random

import matplotlib.pyplot as plt

from stats.constants.habitat import Habitat


class BirdNumberHabitatGraphService:
    filename = 'stats/files/graph/bird_number_habitat.jpg'

    def __init__(self, display: bool):
        from stats.repositories.player_games import PlayerGameRepository

        self.display = display
        self.player_games = PlayerGameRepository.all()
        self.fig, self.ax = plt.subplots()

        self.compute_data()
        self.add_options()
        self.result()

    @staticmethod
    def add_options():
        plt.xlabel('Score')
        plt.ylabel("Nombre total d'oiseau")
        plt.legend(loc='upper left')
        plt.title("Score/Nombre d'oiseau")

    def result(self):
        plt.savefig(self.filename)
        if self.display:
            plt.show()

    def compute_data(self):
        self.draw_games(Habitat.FOREST, 'green', 'Forêt')
        self.draw_games(Habitat.PLAIN, 'gold', 'Plaine')
        self.draw_games(Habitat.SWAMP, 'blue', 'Marais')

    def draw_games(self, habitat, color, label):
        scores = []
        bird_numbers = []
        for player_game in self.player_games:
            scores.append(self.approximate_score(player_game.score))
            birds = player_game.birds.filter(habitat=habitat)
            bird_numbers.append(len(birds))
        self.ax.scatter(scores, bird_numbers, color=color, label=label)

    @staticmethod
    def approximate_score(score):
        epsilon = random.randint(-10, 10)/100
        return score + epsilon

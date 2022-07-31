import matplotlib.pyplot as plt

from stats.constants.habitat import Habitat


class BirdNumberGraphService:
    filename = 'stats/files/graph/bird_number.jpg'

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
        plt.title("Score/Nombre d'oiseau")

    def result(self):
        plt.savefig(self.filename)
        if self.display:
            plt.show()

    def compute_data(self):
        scores = []
        bird_number = []
        for player_game in self.player_games:
            scores.append(player_game.score)
            bird_number.append(len(player_game.birds.all()))
        self.ax.scatter(scores, bird_number)

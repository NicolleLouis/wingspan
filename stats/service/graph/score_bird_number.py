import matplotlib.pyplot as plt

from stats.service.graph.graph import GraphService


class BirdNumberGraphService(GraphService):
    filename = 'stats/files/graph/bird_number.jpg'

    @staticmethod
    def add_options():
        plt.xlabel('Score')
        plt.ylabel("Nombre total d'oiseau")
        plt.title("Score/Nombre d'oiseau")

    def compute_data(self):
        scores = []
        bird_number = []
        for player_game in self.player_games:
            scores.append(player_game.score)
            bird_number.append(len(player_game.birds.all()))
        self.ax.scatter(scores, bird_number)

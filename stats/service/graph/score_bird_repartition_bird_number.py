import matplotlib.pyplot as plt

from stats.service.graph.score_bird_repartition import BirdRepartitionGraphService


class BirdNumberRepartitionGraphService(BirdRepartitionGraphService):
    filename = 'stats/files/graph/bird_number_repartition.jpg'

    def add_options(self):
        plt.ylabel("Nombre d'oiseau")
        plt.title("Répartition au sein des 10 meilleures parties")

        self.ax.legend()

    @staticmethod
    def score_by_habitat(player_game, habitat):
        return len(player_game.birds.filter(habitat=habitat))

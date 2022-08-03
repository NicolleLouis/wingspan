import matplotlib.pyplot as plt

from stats.service.graph.score_bird_repartition import BirdRepartitionGraphService


class BirdScoreRepartitionGraphService(BirdRepartitionGraphService):
    filename = 'stats/files/graph/bird_score_repartition.jpg'

    def add_options(self):
        plt.ylabel('Score de la carte oiseau')
        plt.title("Répartition au sein des 10 meilleures parties")

        self.ax.legend()

    @staticmethod
    def score_by_habitat(player_game, habitat):
        score = 0
        birds = player_game.birds.filter(habitat=habitat)
        for bird in birds:
            score += bird.bird_card.points
        return score

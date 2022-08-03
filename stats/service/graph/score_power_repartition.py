from matplotlib import pyplot as plt

from stats.constants.color import Color
from stats.service.graph.graph import GraphService


class PowerRepartitionGraphService(GraphService):
    filename = 'stats/files/graph/power_color_number_repartition.jpg'

    def __init__(self, **kwargs):
        self.labels = []
        self.browns = []
        self.blues = []
        self.pinks = []
        self.whites = []
        self.empties = []
        self.bottom_blues = []
        self.bottom_pinks = []
        self.bottom_whites = []
        self.bottom_empties = []
        super().__init__(**kwargs)

    @staticmethod
    def label_from_player_game(player_game):
        return f"{player_game.score} ({player_game.user})"

    def sort_data(self):
        self.player_games = sorted(
            self.player_games,
            key=lambda player_game: player_game.score
        )

    def filter_data(self):
        if len(self.player_games) > 10:
            self.player_games = self.player_games[-10:]

    @staticmethod
    def card_by_color(player_game, color):
        return len(player_game.birds.filter(bird_card__bird_power__color=color))

    def generate_dataset(self):
        for player_game in self.player_games:
            self.labels.append(self.label_from_player_game(player_game))
            self.browns.append(self.card_by_color(player_game, Color.BROWN))
            self.whites.append(self.card_by_color(player_game, Color.WHITE))
            self.pinks.append(self.card_by_color(player_game, Color.PINK))
            self.blues.append(self.card_by_color(player_game, Color.BLUE))
            self.empties.append(self.card_by_color(player_game, Color.NOTHING))

    def generate_bottoms(self):
        self.bottom_blues = self.browns
        self.bottom_pinks = self.sum_dataset(self.bottom_blues, self.blues)
        self.bottom_whites = self.sum_dataset(self.bottom_pinks, self.pinks)
        self.bottom_empties = self.sum_dataset(self.bottom_whites, self.whites)

    @staticmethod
    def sum_dataset(dataset_1, dataset_2):
        result = []
        for index, value in enumerate(dataset_1):
            result.append(value + dataset_2[index])
        return result

    def add_data_to_figure(self):
        self.ax.bar(
            self.labels,
            self.browns,
            color="saddlebrown",
            label="Marrons"
        )
        self.ax.bar(
            self.labels,
            self.blues,
            color="lightskyblue",
            label="Bleu",
            bottom=self.bottom_blues
        )
        self.ax.bar(
            self.labels,
            self.pinks,
            color="pink",
            label="Rose",
            bottom=self.bottom_pinks
        )
        self.ax.bar(
            self.labels,
            self.whites,
            color="grey",
            label="Pose",
            bottom=self.bottom_whites
        )
        self.ax.bar(
            self.labels,
            self.empties,
            color="lightgrey",
            label="Nothing",
            bottom=self.bottom_empties
        )
    
    def add_options(self):
        plt.ylabel("Couleur des pouvoirs")
        plt.title("Nombre d'oiseau par couleur de pouvoir")

        self.ax.legend()

    def compute_data(self):
        self.sort_data()
        self.filter_data()
        self.generate_dataset()
        self.generate_bottoms()
        self.add_data_to_figure()

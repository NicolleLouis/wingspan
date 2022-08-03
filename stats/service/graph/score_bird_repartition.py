from stats.constants.habitat import Habitat
from stats.service.graph.graph import GraphService


class BirdRepartitionGraphService(GraphService):
    def __init__(self, **kwargs):
        self.labels = []
        self.forests = []
        self.plains = []
        self.swamps = []
        self.bottom_swamp = []
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
    def score_by_habitat(player_game, habitat):
        raise NotImplementedError

    def generate_dataset(self):
        for player_game in self.player_games:
            self.labels.append(self.label_from_player_game(player_game))
            self.forests.append(self.score_by_habitat(player_game, Habitat.FOREST))
            self.plains.append(self.score_by_habitat(player_game, Habitat.PLAIN))
            self.swamps.append(self.score_by_habitat(player_game, Habitat.SWAMP))

        for index, forest in enumerate(self.forests):
            self.bottom_swamp.append(forest + self.plains[index])
    
    def add_data_to_figure(self):
        self.ax.bar(
            self.labels,
            self.forests,
            color="green",
            label="Forest"
        )
        self.ax.bar(
            self.labels,
            self.plains,
            color="gold",
            label="Plaine",
            bottom=self.forests
        )
        self.ax.bar(
            self.labels,
            self.swamps,
            color="blue",
            label="Marais",
            bottom=self.bottom_swamp
        )

    def compute_data(self):
        self.sort_data()
        self.filter_data()
        self.generate_dataset()
        self.add_data_to_figure()

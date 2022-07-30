from stats.models import PlayerGame


class PlayerGameRepository:
    @staticmethod
    def all():
        return PlayerGame.objects.all()

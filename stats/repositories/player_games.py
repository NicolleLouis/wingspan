from stats.models import PlayerGame


class PlayerGameRepository:
    @staticmethod
    def all():
        return PlayerGame.objects.all()

    @staticmethod
    def by_user(user):
        return PlayerGame.objects.filter(user=user)

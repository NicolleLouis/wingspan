from stats.models import BirdPower


class BirdPowerRepository:
    @staticmethod
    def get_or_create(color, type, text) -> BirdPower:
        bird_power, created = BirdPower.objects.get_or_create(
            color=color,
            type=type,
            name=text,
        )
        return bird_power

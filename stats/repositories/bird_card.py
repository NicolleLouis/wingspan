from stats.models import BirdCard


class BirdCardRepository:
    @staticmethod
    def get_or_create_by_latin_name(latin_name: str) -> BirdCard:
        bird_card, created = BirdCard.objects.get_or_create(
            latin_name=latin_name
        )
        return bird_card

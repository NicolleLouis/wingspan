from django.core.management.base import BaseCommand

from stats.service.graph.score_bird_number_habitat import BirdNumberHabitatGraphService


class Command(BaseCommand):
    def handle(self, *args, **options):
        BirdNumberHabitatGraphService(True)

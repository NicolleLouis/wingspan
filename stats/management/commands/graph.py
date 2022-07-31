from django.core.management.base import BaseCommand

from stats.service.graph.engine_score import EngineGraphService
from stats.service.graph.score_bird_number import BirdNumberGraphService
from stats.service.graph.score_bird_number_habitat import BirdNumberHabitatGraphService


class Command(BaseCommand):
    def handle(self, *args, **options):
        EngineGraphService(False)
        BirdNumberGraphService(False)
        BirdNumberHabitatGraphService(False)

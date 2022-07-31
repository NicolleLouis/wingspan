from django.core.management.base import BaseCommand

from stats.service.graph.engine_score import EngineGraphService


class Command(BaseCommand):
    def handle(self, *args, **options):
        EngineGraphService(True)

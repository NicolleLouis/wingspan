from django.core.management.base import BaseCommand

from stats.service.graph.score_bird_repartition import BirdRepartitionGraphService


class Command(BaseCommand):
    def handle(self, *args, **options):
        BirdRepartitionGraphService(display=True)

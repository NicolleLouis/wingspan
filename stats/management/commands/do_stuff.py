from django.core.management.base import BaseCommand

from stats.service.graph.score_power_repartition import PowerRepartitionGraphService


class Command(BaseCommand):
    def handle(self, *args, **options):
        PowerRepartitionGraphService(display=True)

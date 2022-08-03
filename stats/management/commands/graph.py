from django.core.management.base import BaseCommand

from stats.service.graph.all_graph import AllGraph


class Command(BaseCommand):
    def handle(self, *args, **options):
        AllGraph(display=True)

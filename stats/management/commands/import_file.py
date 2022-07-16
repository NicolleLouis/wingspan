from django.core.management.base import BaseCommand

from stats.service.import_file import ImportFile


class Command(BaseCommand):
    def handle(self, *args, **options):
        lines = ImportFile.read_file()
        filtered_lines = ImportFile.filter_lines(lines)

        for line in filtered_lines:
            bird_card = ImportFile.get_or_create_bird_card(line)
            print(bird_card)

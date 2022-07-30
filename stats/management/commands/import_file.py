from django.core.management.base import BaseCommand

from stats.service.import_file import ImportFile


class Command(BaseCommand):
    def handle(self, *args, **options):
        lines = ImportFile.read_file()
        filtered_lines = ImportFile.filter_lines(lines)

        for line in filtered_lines:
            bird_card = ImportFile.get_or_create_bird_card(line)
            ImportFile.save_base_info(line, bird_card)
            ImportFile.save_habitat_info(line, bird_card)
            ImportFile.save_nest_info(line, bird_card)
            ImportFile.save_extension(line, bird_card)
            ImportFile.save_extension(line, bird_card)
            ImportFile.save_power(line, bird_card)

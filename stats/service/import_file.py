import csv

from stats.repositories.bird_card import BirdCardRepository


class ImportFile:
    filepath = 'stats/files/card_list.csv'

    @classmethod
    def read_file(cls):
        file = open(cls.filepath, mode='r')
        lines = csv.reader(file, delimiter=';')
        return lines

    @classmethod
    def filter_lines(cls, lines):
        filtered_lines = filter(
            lambda line: cls.should_read_line(line),
            lines
        )
        return filtered_lines

    @staticmethod
    def should_read_line(line):
        extension = line[2]
        return extension in ['originalcore', 'european']

    @staticmethod
    def get_or_create_bird_card(line):
        latin_name = line[1]
        return BirdCardRepository.get_or_create_by_latin_name(latin_name)



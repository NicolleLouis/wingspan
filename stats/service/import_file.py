import csv

from stats.constants.color import Color
from stats.constants.extension import Extension
from stats.constants.nest import Nest
from stats.constants.power_type import PowerType
from stats.repositories.bird_card import BirdCardRepository

from typing import TYPE_CHECKING

from stats.repositories.bird_power import BirdPowerRepository

if TYPE_CHECKING:
    from stats.models import BirdCard


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

    @staticmethod
    def save_base_info(line, bird: 'BirdCard'):
        english_name = line[0]
        bird.english_name = english_name
        victory_point = line[9]
        bird.points = victory_point
        eggs = line[11]
        bird.egg_number = eggs
        cost = line[25]
        bird.price = cost
        bird.save()

    @staticmethod
    def convert_to_boolean(raw_string):
        return raw_string == 'X'

    @classmethod
    def save_habitat_info(cls, line, bird: 'BirdCard'):
        is_forest = cls.convert_to_boolean(line[13])
        is_plain = cls.convert_to_boolean(line[14])
        is_swamp = cls.convert_to_boolean(line[15])

        bird.can_live_in_forest = is_forest
        bird.can_live_in_plain = is_plain
        bird.can_live_in_swamp = is_swamp
        bird.save()

    @staticmethod
    def save_nest_info(line, bird: 'BirdCard'):
        raw_nest = line[10]
        nest_conversion = {
            'Platform': Nest.PLATFORM,
            'Ground': Nest.GROUND,
            'Bowl': Nest.BOWL,
            'Wild': Nest.BONUS,
            'Cavity': Nest.CAVITY,
            '': Nest.NOTHING
        }
        bird.nest_type = nest_conversion[raw_nest]
        bird.save()

    @staticmethod
    def save_extension(line, bird: 'BirdCard'):
        raw_extension = line[2]
        extension_conversion = {
            'originalcore': Extension.CORE,
            'european': Extension.EUROPA,
        }
        extension = extension_conversion[raw_extension]
        bird.extension = extension
        bird.save()
    
    @staticmethod
    def save_power(line, bird: 'BirdCard'):
        raw_color = line[3]
        raw_category = line[4]
        text = line[5]
        color_conversion = {
            'Brown': Color.BROWN,
            'White': Color.WHITE,
            'Pink': Color.PINK,
            'Teal': Color.BLUE,
            '': Color.NOTHING,
        }
        color = color_conversion[raw_color]
        category_conversion = {
            'Caching Food': PowerType.FOOD,
            'Egg-laying': PowerType.EGG,
            'Card-drawing': PowerType.CARD_DRAW,
            'Flocking': PowerType.REPRODUCTION,
            'Food from Supply': PowerType.FOOD,
            'Hunting/Fishing': PowerType.HUNT,
            '': None,
            'Food from Birdfeeder': PowerType.FOOD,
            'Other': PowerType.OTHER,
            'Food-related': PowerType.FOOD,
            'Hunting and Fishing': PowerType.HUNT,
            'Hunting and fishing': PowerType.HUNT,
            'Tucking': PowerType.REPRODUCTION,
        }
        category = category_conversion[raw_category]
        power = BirdPowerRepository.get_or_create(
            color=color,
            type=category,
            text=text,
        )
        bird.bird_power = power
        bird.save()
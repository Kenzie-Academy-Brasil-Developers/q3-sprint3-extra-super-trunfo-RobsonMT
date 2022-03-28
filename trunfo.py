import itertools
from os import getenv
from random import choices, sample
from dotenv import load_dotenv
from json_handler import read_json, write_json


# Não delete a linha abaixo, carregamento de variáveis de ambiente
load_dotenv()


class Trunfo:
    # Desenvolva sua classe abaixo
    FILENAME = getenv("FILENAME")
    SCORE = {"player_1": 0, "player_2": 0, "draw": 0}
    ATTRIBUTES = ["intelligence", "power", "strenght", "agility", "vitality"]

    def __init__(
        self,
        name: str,
        intelligence: int,
        power: int,
        strenght: int,
        agility: int,
        vitality: int,
    ) -> None:
        self.name = name
        self.intelligence = intelligence
        self.power = power
        self.strenght = strenght
        self.agility = agility
        self.vitality = vitality

    def register_card(self):
        write_json(self.FILENAME, self.__dict__)

    @classmethod
    def list_all_super_heroes(cls):
        return read_json(cls.FILENAME)

    @classmethod
    def get_players_decks(cls):

        decks_of_cards = read_json(cls.FILENAME)

        if not len(decks_of_cards) % 2 == 0:
            return None

        shuffled_cards = sample(decks_of_cards, k=len(decks_of_cards))

        num_of_card_to_player = int(len(shuffled_cards) / 2)

        players1_cards = shuffled_cards[:num_of_card_to_player:]
        players2_cards = shuffled_cards[num_of_card_to_player::]

        return {"player_1": players1_cards, "player_2": players2_cards}

    @classmethod
    def compare_cards(cls):

        decks_of_cards = cls.list_all_super_heroes()

        if not len(decks_of_cards) % 2 == 0:
            return None

        players_cards = cls.get_players_decks()

        attribute_random = choices(cls.ATTRIBUTES, k=1)[0]

        p1_attributes_sum = 0
        p2_attributes_sum = 0

        for card in players_cards["player_1"]:
            p1_attributes_sum += card[attribute_random]

        for card in players_cards["player_2"]:
            p2_attributes_sum += card[attribute_random]

        if p1_attributes_sum > p2_attributes_sum:
            cls.SCORE.update({"player_1": cls.SCORE["player_1"] + 1})
        if p1_attributes_sum < p2_attributes_sum:
            cls.SCORE.update({"player_2": cls.SCORE["player_2"] + 1})
        if p1_attributes_sum == p2_attributes_sum:
            cls.SCORE.update({"draw": cls.SCORE["draw"] + 1})

        return cls.SCORE

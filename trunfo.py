import itertools
import json
from os import getenv
from random import choices, sample
from dotenv import load_dotenv

load_dotenv()

class Trunfo:
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
         with open(self.FILENAME, "r") as in_file:
            json_list = json.load(in_file)
            json_list.append(self.__dict__)

            with open(self.FILENAME, "w") as out_file:
                json.dump(json_list, out_file, indent=2)

    @classmethod
    def list_all_super_heroes(cls):
        with open(cls.FILENAME, "r") as json_file:
            return json.load(json_file)

    @classmethod
    def get_players_decks(cls):

        decks_of_cards = cls.list_all_super_heroes()

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

        p1_att_value = 0
        p2_att_value = 0

        for card in zip(players_cards["player_1"], players_cards["player_2"]):
            p1_att_value = card[0][attribute_random]
            p2_att_value = card[1][attribute_random]

            if p1_att_value > p2_att_value:
                cls.SCORE.update({"player_1": cls.SCORE["player_1"] + 1})
            if p1_att_value < p2_att_value:
                cls.SCORE.update({"player_2": cls.SCORE["player_2"] + 1})
            if p1_att_value == p2_att_value:
                cls.SCORE.update({"draw": cls.SCORE["draw"] + 1})

        return cls.SCORE

